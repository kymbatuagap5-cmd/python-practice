import os
import csv
import json
#task1
class FileManager():
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found.")
        return False

    def create_output_folder(self, folder='output'):
        print("\nChecking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")

#task2
class DataLoader():
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("\nLoading data...")
        try:
            with open(self.filename, encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.students = list(reader)
                print(f"Data loaded successfully: {len(self.students)} students")
                return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")  
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None  

    def preview(self, n=5):
        if not self.students:
            return
        print(f"\nFirst {n} rows:")
        print("-" * 30)
        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
        print("-" * 30)
        print("\n")

#task3
class DataAnalyser():
    def __init__(self, students):
        self.students = students
        self.result = {}
    def analyse(self):
        country_counts = {}
        for student in self.students:
            try:
                float(student.get('GPA', 0)) 
            except ValueError:
                print(f"Warning: could not convert value for student {student.get('student_id')} — skipping row.")
                continue
            except TypeError:
                continue
            country = student.get("country", "Unknown")
            country_counts[country] = country_counts.get(country, 0) + 1
        top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        self.result = {
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3": [{"country": c, "count": n} for c, n in top_3]
        }
        return self.result 
    def print_results(self):
        if not self.result:
            print("No analysis results found. Run .analyse() first.")
            return
        print("-" * 30)
        print("Country Analysis")
        print("-" * 30)
        print(f"Total countries : {self.result['total_countries']}")
        print("Top 3 Countries:")
        for i, item in enumerate(self.result['top_3'], start=1):
            print(f"{i}. {item['country']} : {item['count']} students")
        print("-" * 30) 

#task4
class ResultSaver():
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path
    def save_json(self):
        try:
            with open(self.output_path, "w") as f:
                json.dump(self.result, f,indent=4)  
                print(f"Result saved to {self.output_path}")  
        except Exception as e:
            print(f"An unexpected error occurred while writing the file: {e}")
            return None       

#task5
fm = FileManager('students.csv')
if not fm.check_file():
    print('Stopping program.')
    exit()
fm.create_output_folder()
dl = DataLoader('students.csv')  
dl.load()
dl.preview()
analyser = DataAnalyser(dl.students)  
analyser.analyse()
analyser.print_results()
saver = ResultSaver(analyser.result, 'output/result.json')
saver.save_json()
