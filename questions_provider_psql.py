from question import Question
import logging
import os
import psycopg2

class QuestionsProviderPsql:

    def __init__(self, settings_provider):
        self.database_url = settings_provider.settings['database_url']
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_questions(self):
        
        questions = list()

        try:
            self.connection = psycopg2.connect(self.database_url, sslmode='require')
            self.logger.info("PostgreSQL connection is opened")

            with self.connection.cursor() as cur:
                query = "SELECT * FROM questions;"
                cur.execute(query)
                questions_records = cur.fetchall() 

                n_records = len(questions_records)
                if n_records == 0:
                    self.logger.error("No questions in the questions table")
                else:
                    self.logger.info("select query to question table returned %d records" % n_records)


                for row in questions_records:
                    text = row[1]
                    hint = row[2]
                    answer = row[3]
                    success_message = row[4]
                    fail_message = row[5]
                    question = Question(text, hint, answer, success_message, fail_message)
                    questions.append(question)

        except (Exception, psycopg2.Error) as error :
            self.logger.error("Error while fetching data from PostgreSQL: " + error)
            questions = []

        finally:
            # Closing database connection.
            if(self.connection):
                self.connection.close()
                self.logger.info("PostgreSQL connection is closed")

        return questions