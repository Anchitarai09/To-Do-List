# python program to create a simple to-do list application
def main():
    tasks=[]
    while True:
       print("\n =======to-do list========")
       print("1.add the task")
       print("2.shows the task")
       print("3.Mark task as done")
       print("4.Exit")

       choice=input("Enter your choice : ")

       if choice=='1':
           print()
           n_tasks=int(input("How May Task you want to add : "))

           for i in range(n_tasks):
               task=input("Enter the task :  ")
               tasks.append({"task":task,"done":False})
               print("task added!")
       elif choice == '2':
           print("\ntasks:")
           for index, task in enumerate(tasks):
               status="Done" if task["done"] else "Not done"
               print(f"{index+1}.{task['task']} - {status}")
       elif choice=='3':
           task_index=int(input("Enter the task number to mark as done: ")) -1
           if 0 <= task_index < len(tasks):
               tasks[task_index]["done"]=True
               print("Task marked as done!")
           else:
              print("Invalid task number.")          
       elif choice== '4':
           print("Exiting the to-do list.")
           break
       else:
           print("Invalid choice.please try again")
if __name__=="__main__":
    main()       