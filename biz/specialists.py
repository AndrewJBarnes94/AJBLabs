import openai
import sqlite3
import imaplib
import email
from email.header import decode_header

class ChatGPT:
    """
    Class for interacting with OpenAI's ChatGPT model.
    
    Attributes:
        api_key (str): API key for OpenAI.
        model_name (str): The specific GPT model name to use.
    """
    
    def __init__(self, api_key, model_name="text-davinci-003"):
        """
        Initializes an instance of ChatGPT.
        
        Args:
            api_key (str): OpenAI API key.
            model_name (str, optional): Name of the GPT model to use. Defaults to "text-davinci-003".
        """
        self.api_key = api_key
        self.model_name = model_name
        openai.api_key = self.api_key  # Set the OpenAI API key

    def get_prompt(self, prompt):
        """
        Retrieve a prompt from the user.
        
        Args:
            prompt (str): The question or message from the user.

        Returns:
            str: The same prompt (can be enhanced for pre-processing in future).
        """
        return prompt

    def fetch_response(self, question):
        """
        Send a question to ChatGPT and retrieve the model's response.
        
        Args:
            question (str): The question to ask the model.

        Returns:
            str: The model's response.
        """
        # Make a completion request to OpenAI with the specified model and parameters
        completion = openai.Completion.create(
            model=self.model_name,
            prompt=question,
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        # Extract and return the text response from the model's completion
        return completion["choices"][0]["text"].strip()


class Files:
    """
    Class to convert files between binary representations and their original formats.
    
    Attributes:
        input_path (str): Path to the input file.
        output_path (str): Path to the output file.
    """

    def __init__(self, input_path, output_path):
        """
        Initializes an instance of FileBinaryConverter.
        
        Args:
            input_path (str): Path to the file to be read.
            output_path (str): Path to the file to be written.
        """
        self.input_path = input_path
        self.output_path = output_path

    def file_to_binary(self):
        """
        Convert the content of a file to its binary representation.
        """
        # Read the input file in binary mode
        with open(self.input_path, 'rb') as file:
            file_data = file.read()

        # Convert file data to binary representation
        binary_representation = ' '.join(f"{byte:08b}" for byte in file_data)

        # Write the binary representation to the output file
        with open(self.output_path, 'w') as file:
            file.write(binary_representation)

        print(f"Binary representation of {self.input_path} saved to {self.output_path}")

    def binary_to_file(self):
        """
        Convert a binary representation back to its original file content.
        """
        # Read the input file with binary representation
        with open(self.input_path, 'r') as file:
            binary_representation = file.read()

        # Split the binary representation by spaces and convert back to bytes
        byte_data = bytes(int(binary_chunk, 2) for binary_chunk in binary_representation.split())

        # Write the bytes to the output file
        with open(self.output_path, 'wb') as file:
            file.write(byte_data)

        print(f"Original file from binary representation at {self.input_path} saved to {self.output_path}")

    def read_binary_of_file(input_path):
        # Read the input file in binary mode
        with open(input_path, 'rb') as file:
            file_data = file.read()

        # Convert file data to binary representation
        binary_representation = ' '.join(f"{byte:08b}" for byte in file_data)
        
        return binary_representation
    
    def readTXTfile(prompt_file):
        with open(prompt_file, "r") as file:
            prompt = file.read()
        
        return prompt

class SQLiteDBManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def execute(self, query, params=None):
        if not self.conn:
            self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

    def fetch_one(self):
        return self.cursor.fetchone()
    
    def fetch_all(self):
        return self.cursor.fetchall()
    
    def create_table(self, table_name, columns):
        columns_str = ', '.join([f'{col_name} {col_type}' for col_name, col_type in columns.items()])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.execute(create_table_query)

    def insert(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute(insert_query, tuple(data.values()))

class EmailReader:
    def __init__(self, imap_server, email_address, password):
        self.imap_server = imap_server
        self.email_address = email_address
        self.password = password
        self.imap = None
    
    def connect(self):
        self.imap = imaplib.IMAP4_SSL(self.imap_server)
        self.imap.login(self.email_address, self.password)
    
    def disconnect(self):
        if self.imap:
            self.imap.close()
            self.imap.logout()
            self.imap = None

    def fetch_recent_emails(self, num_emails=25):
        self.imap.select("Inbox")
        _, msgnums = self.imap.search(None, "ALL")
        msgnums = msgnums[0].split()[-num_emails:]

        emails = []
        for msgnum in msgnums:
            _, data = self.imap.fetch(msgnum, "(RFC822)")
            message = email.message_from_bytes(data[0][1])
            emails.append(message)

        return emails
    
    def get_email_details(self, message):
        subject, encoding = decode_header(message["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8', errors='replace')
        
        from_, encoding = decode_header(message["From"])[0]
        if isinstance(from_, bytes):
            from_ = from_.decode(encoding if encoding else 'utf-8', errors='replace')
        
        date, encoding = decode_header(message["Date"])[0]
        if isinstance(date, bytes):
            date = date.decode(encoding if encoding else 'utf-8', errors='replace')
        
        content = ""
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                charset = part.get_content_charset()
                try:
                    content = part.get_payload(decode=True).decode(charset if charset else 'utf-8')
                except UnicodeDecodeError:
                    content = part.get_payload(decode=True).decode('utf-8', errors='replace')
                break
        
        return {
            "From": from_,
            "Date": date,
            "Subject": subject,
            "Content": content
        }