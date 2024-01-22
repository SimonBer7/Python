import os


class FileDatabase():

    def __init__(self,file_path,file_encoding):
        self.file_path = file_path
        self.file_encoding =file_encoding
        self.application = None

    def get_task_list(self):
        task_list = list()
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding=self.file_encoding) as f:
                task_list = f.readlines()
        return task_list

    def get_first_task(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding=self.file_encoding) as f:
                first_task = f.readline()
        return first_task

    def add_task(self, new_task):
        if os.path.exists(self.file_path):
            mode = "a"
        else:
            mode = "w"
        with open(self.file_path, mode, encoding=self.file_encoding) as f:
            f.write(new_task + "\n")
            f.flush()

    def remove_task_list(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def remove_first_task(self):
        with open(self.file_path, "r", encoding=self.file_encoding) as f:
            tasks = f.readlines()
        tasks.pop(0)
        with open(self.file_path, "w", encoding=self.file_encoding) as f:
            for task in tasks:
                f.write(str(task))




