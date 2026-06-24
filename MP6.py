import os

class Project:
    """Class representing an individual copy-typing project."""
    def __init__(self, id_num, title, size, priority):
        self.id_num = int(id_num)
        self.title = str(title)
        self.size = int(size)
        self.priority = int(priority)

    def to_file_format(self):
        """Returns string format with clear data labels for file storage."""
        return f"ID:{self.id_num}|TITLE:{self.title}|SIZE:{self.size}|PRIORITY:{self.priority}\n"

    def __str__(self):
        """Returns user-friendly string format."""
        return f"ID: {self.id_num} | Title: {self.title} | Size: {self.size} pages | Priority: {self.priority}"


class ProjectScheduler:
    """Class handling file operations, queuing, and scheduling logic."""
    def __init__(self, projects_file="projects.txt", completed_file="completed_projects.txt"):
        self.projects_file = projects_file
        self.completed_file = completed_file
        self.queue = []
        self.schedule_created = False

    def load_all_projects(self):
        """Helper to read and parse labeled data from the text file."""
        projects = []
        if not os.path.exists(self.projects_file):
            return projects
        
        try:
            with open(self.projects_file, "r") as file:
                for line in file:
                    if not line.strip():
                        continue
                    
                    parts = line.strip().split("|")
                    if len(parts) == 4:
                        try:
                            # Strip out the labels ("ID:", "TITLE:", etc.) to extract raw values
                            id_val = parts[0].replace("ID:", "").strip()
                            title_val = parts[1].replace("TITLE:", "").strip()
                            size_val = parts[2].replace("SIZE:", "").strip()
                            priority_val = parts[3].replace("PRIORITY:", "").strip()
                            
                            projects.append(Project(id_val, title_val, size_val, priority_val))
                        except IndexError:
                            continue
                            
        except (IOError, ValueError) as e:
            print(f"[Error reading file: {e}]")
        return projects

    def save_all_projects(self, projects):
        """Helper to rewrite the pending projects file with data labels."""
        try:
            with open(self.projects_file, "w") as file:
                for proj in projects:
                    file.write(proj.to_file_format())
        except IOError as e:
            print(f"[Error writing file: {e}]")

    def input_project_details(self):
        """Option 1: Collects information and stores it into the text file."""
        print("\n--- Input Project Details ---")
        try:
            id_num = int(input("Enter ID Number (Integer): "))
            
            # Check for duplicate ID numbers
            existing_projects = self.load_all_projects()
            if any(p.id_num == id_num for p in existing_projects):
                print("Error: A project with this ID Number already exists!")
                return

            title = input("Enter Title: ").strip()
            if not title:
                raise ValueError("Title cannot be blank.")
                
            size = int(input("Enter Size (Number of pages): "))
            if size <= 0:
                raise ValueError("Size must be a positive integer.")
                
            priority = int(input("Enter Priority (Lower number = higher priority): "))
            
            new_project = Project(id_num, title, size, priority)
            
            # Append labeled line to file
            with open(self.projects_file, "a") as file:
                file.write(new_project.to_file_format())
                
            print(f"Success: Project '{title}' successfully saved!")
            self.schedule_created = False
            
        except ValueError as e:
            print(f"Input Error: {e}. Please enter correct data types.")
        except IOError as e:
            print(f"File Error: Could not save data. {e}")

    def view_one_project(self):
        """Option 2A: Search and view one specific project using its ID Number."""
        print("\n--- View One Project ---")
        try:
            search_id = int(input("Enter Project ID to search: "))
            projects = self.load_all_projects()
            for proj in projects:
                if proj.id_num == search_id:
                    print("\nProject Found:")
                    print(proj)
                    return
            print("Project not found.")
        except ValueError:
            print("Invalid input! ID must be an integer value.")

    def view_completed_projects(self):
        """Option 2B: Display all projects that have been completed."""
        print("\n--- Completed Projects ---")
        if not os.path.exists(self.completed_file) or os.path.getsize(self.completed_file) == 0:
            print("No completed projects found.")
            return
        
        try:
            with open(self.completed_file, "r") as file:
                count = 0
                for line in file:
                    if not line.strip():
                        continue
                    parts = line.strip().split("|")
                    if len(parts) == 4:
                        id_val = parts[0].replace("ID:", "").strip()
                        title_val = parts[1].replace("TITLE:", "").strip()
                        size_val = parts[2].replace("SIZE:", "").strip()
                        priority_val = parts[3].replace("PRIORITY:", "").strip()
                        
                        proj = Project(id_val, title_val, size_val, priority_val)
                        print(proj)
                        count += 1
                print(f"Total Completed Projects: {count}")
        except IOError as e:
            print(f"File Error: Could not read completed log. {e}")

    def view_all_projects(self):
        """Option 2C: Display all projects currently pending in the text file."""
        print("\n--- All Received Pending Projects ---")
        projects = self.load_all_projects()
        if not projects:
            print("No pending projects in record.")
            return
        for proj in projects:
            print(proj)
        print(f"Total Pending Projects: {len(projects)}")

    def create_schedule(self):
        """Option 3A: Automatically create a sorted priority queue from file records."""
        print("\n--- Create Schedule ---")
        projects = self.load_all_projects()
        if not projects:
            print("Cannot create schedule: No pending projects exist in the record file.")
            self.queue = []
            self.schedule_created = False
            return

        # Sorting rule: Priority ascending, then Size ascending
        self.queue = sorted(projects, key=lambda p: (p.priority, p.size))
        self.schedule_created = True
        
        print("Queue successfully generated! Current Schedule Queue order:")
        self.display_queue()

    def view_schedule(self):
        """Option 3B: View the current schedule queue if created."""
        print("\n--- View Schedule ---")
        if not self.schedule_created:
            print("Prompt: The schedule has not been created yet! Please choose 'Create Schedule' first.")
            return
        if not self.queue:
            print("The schedule queue is currently empty.")
            return
        self.display_queue()

    def display_queue(self):
        """Helper to print the exact state of the scheduling queue."""
        for index, proj in enumerate(self.queue, start=1):
            print(f"[{index}] ID: {proj.id_num} | Title: {proj.title} (Priority: {proj.priority}, Size: {proj.size} pgs)")

    def get_a_project(self):
        """Option 4: Remove topmost project from queue and record it to Completed file."""
        print("\n--- Get a Project ---")
        if not self.schedule_created:
            print("Prompt: Cannot fetch a job. Please create the schedule queue first.")
            return
        if not self.queue:
            print("The schedule queue is empty! No projects left to process.")
            return

        completed_proj = self.queue.pop(0)
        print(f"Processing Complete: Topmost project '{completed_proj.title}' (ID: {completed_proj.id_num}) has been processed.")

        # 1. Place the removed project's details into the Completed Projects file
        try:
            with open(self.completed_file, "a") as file:
                file.write(completed_proj.to_file_format())
        except IOError as e:
            print(f"File handling Error: Could not log completion data. {e}")

        # 2. Update the main pending file list to remove the completed project
        all_pending = self.load_all_projects()
        all_pending = [p for p in all_pending if p.id_num != completed_proj.id_num]
        self.save_all_projects(all_pending)

        # 3. Display updated queue
        print("\nUpdated Schedule Queue State:")
        if self.queue:
            self.display_queue()
        else:
            print("[Queue is now empty]")


def main_menu():
    scheduler = ProjectScheduler()
    
    while True:
        print("\n==============================================")
        print("     COPY-TYPING PROJECT SCHEDULER SYSTEM     ")
        print("==============================================")
        print("1. Input Project Details")
        print("2. View Projects")
        print("3. Schedule Projects")
        print("4. Get a Project")
        print("5. Exit")
        print("==============================================")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            scheduler.input_project_details()
            
        elif choice == "2":
            print("\n  [View Menu Options]")
            print("  A. One Project (Search by ID)")
            print("  B. Completed Projects")
            print("  C. All Projects")
            sub_choice = input("  Select option (A/B/C): ").strip().upper()
            if sub_choice == "A":
                scheduler.view_one_project()
            elif sub_choice == "B":
                scheduler.view_completed_projects()
            elif sub_choice == "C":
                scheduler.view_all_projects()
            else:
                print("Invalid sub-menu option selection.")
                
        elif choice == "3":
            print("\n  [Schedule Menu Options]")
            print("  A. Create Schedule")
            print("  B. View Schedule")
            sub_choice = input("  Select option (A/B): ").strip().upper()
            if sub_choice == "A":
                scheduler.create_schedule()
            elif sub_choice == "B":
                scheduler.view_schedule()
            else:
                print("Invalid sub-menu option selection.")
                
        elif choice == "4":
            scheduler.get_a_project()
            
        elif choice == "5":
            print("\nThank you for using the system. Closing program... Goodbye!")
            break
        else:
            print("Invalid Choice! Please pick a configuration option between 1 and 5.")

if __name__ == "__main__":
    main_menu()