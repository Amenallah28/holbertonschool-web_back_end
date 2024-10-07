#!/usr/bin/env python3
""" module that containes functions used
to obstruct the log message and return it """
import re
from typing import List
import logging
import mysql.connector
import os

PII_FIELDS = ("name", "ssn", "password", "phone", "email")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ function used to obstruct the log message and return it """

    for i in fields:
        message = re.sub(f"(?<={i}=)[^{separator}]+", redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
          constarctor method that initializes fields property
          and assigns the format to RedactingFormatter method
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        The method that formats the logRecord object
        """
        logging.basicConfig(format=self.FORMAT, level=logging.INFO)
        message = filter_datum(self.fields, self.REDACTION,
                               super().format(record), self.SEPARATOR)
        return message


def get_logger() -> logging.Logger:
    """ method to create a logger
        handler = streamhandler
        formatter = RedactingFormatter"""
    mylogger = logging.getLogger("user_data")
    mylogger.setLevel(logging.INFO)
    myhandler = logging.StreamHandler()
    myformatter = RedactingFormatter(PII_FIELDS)
    myhandler.setFormatter(myformatter)
    mylogger.addHandler(myhandler)
    mylogger.propagate = False


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ funtion to connect to a database and return
        the connection object """
    dbUsername = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    dbHost = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    dbPassword = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    dbName = os.getenv("PERSONAL_DATA_DB_NAME")
    dbOBJ = mysql.connector.connect(host=dbHost, user=dbUsername,
                                    password=dbPassword, database=dbName)
    return dbOBJ
