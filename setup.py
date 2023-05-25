import pandas as pd
 
def csv_to_markdown():        

    file = open("README.md", "w", encoding="UTF-8")

    main_heading = "# Machine Learning and Data Science resources \n"
    file.write(main_heading)

    tutorial_heading = "## Math, Machine Learning and Data Science tutorials \n"
    file.write(tutorial_heading)

    course_heading = "#Tutorial | #Paid/Free | #Author | #Language"
    course_heading += "\n  --- | --- | --- | --- \n"
    file.write(course_heading)
        
    data = pd.read_csv("resources.csv")

    learning_resouces = data [(data ["Category"] == "Learning")]
    learn = ""
    for index, row in learning_resouces.iterrows():
        learn += "[" + row['Title'] + "](" + row['Link'] + ") | " + row['Paid'] + " | " + row['Authors'] + " | " + row['Language'] + "\n"
    file.write(learn)

    interviews_heading = "## Interview questions \n"
    interviews_heading += "#Resource | #Type"
    interviews_heading += "\n  --- | --- \n"
    file.write(interviews_heading)

    interview_resouces = data [(data ["Category"] == "Interview")]
    interview = ""
    for index, row in interview_resouces.iterrows():
        interview += "[" + row['Title'] + "](" + row['Link'] + ") | " + row['Type'] + "\n"

    file.write(interview)

    file.close()

    print("The markdown file has been created!!!")

csv_to_markdown()

