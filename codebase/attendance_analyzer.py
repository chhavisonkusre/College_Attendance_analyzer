import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("attendance_data.csv")

print("\nCOLLEGE ATTENDANCE ANALYZER\n")

valid_rows= []
invalid_count= 0

for i, row in df.iterrows():
    held= row["Classes_Held"]
    attended= row["Classes_Attended"]

    if held <= 0:
        print(f"Row {i+1}: Invalid classes held. Skipped.")
        invalid_count += 1
    elif attended < 0:
        print(f"Row {i+1}: Negative attendance. Skipped.")
        invalid_count += 1
    elif attended > held:
        print(f"Row {i+1}: Attendance exceeds classes held. Skipped.")
        invalid_count += 1
    else:
        valid_rows.append(row)

df=pd.DataFrame(valid_rows)

print("\nDATA VALIDATION SUMMARY")
print("Total records:", len(valid_rows)+invalid_count)
print("Valid records:", len(valid_rows))
print("Invalid records:", invalid_count)

print("\nValid attendance records:\n")
print(df)

df["Percentage"]=(df["Classes_Attended"] / df["Classes_Held"]) *100

while True:
    print("\n CHOOSE AN OPTION:")
    print("1. Attendance Percentage")
    print("2. Shortage List")
    print("3. Subject-wise Average and Charts")
    print("4. Student-wise Summary")
    print("5. Exit")

    choice=input("\nEnter your choice: ")

    if choice == "1":
        print("\nAttendance Percentages:\n")
        print(df[["Name", "Subject", "Percentage"]].round(2))

    elif choice == "2":
        shortage= df[df["Percentage"] < 75]

        if shortage.empty:
            print("No student below 75%.")
        else:
            print("\nStudents Below 75%:\n")
            print(shortage[["Name", "Subject", "Percentage"]].round(2))

    elif choice == "3":
        average=df.groupby("Subject")["Percentage"].mean()

        print("\nSubject-wise Average:\n")
        print(average.round(2))

        average.plot(kind="bar", title="Subject-wise Average Attendance")
        plt.ylabel("Attendance Percentage")
        plt.show()

        df["Status"]=df["Percentage"].apply(lambda x: "Eligible" if x >= 75 else "Shortage")
        df["Status"].value_counts().plot(kind="pie", autopct="%1.1f%%", title="Attendance Status")
        plt.ylabel("")
        plt.show()

    elif choice == "4":
        summary=df.groupby("Name").agg(Total_Held=("Classes_Held", "sum"),Total_Attended=("Classes_Attended", "sum"))

        summary["Percentage"]= (summary["Total_Attended"] / summary["Total_Held"]) *100

        print("\nStudent-wise Attendance Summary:")
        print(summary.round(2))

    elif choice == "5":
        print("\nThank you for using College Attendance Analyzer!\n")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")

