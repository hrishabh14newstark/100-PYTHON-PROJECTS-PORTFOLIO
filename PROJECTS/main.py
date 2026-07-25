import os
import json
import sys
import subprocess
import shutil

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(WORKSPACE, "portfolio_data.json")

# ANSI Color Codes for Windows/Unix terminal
CLR_HEADER = "\033[95m"
CLR_BLUE = "\033[94m"
CLR_CYAN = "\033[96m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_BOLD = "\033[1m"
CLR_UNDERLINE = "\033[4m"
CLR_RESET = "\033[0m"

# Initialize console colors for Windows command prompt if needed
if sys.platform == "win32":
    os.system("color")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def load_data():
    if not os.path.exists(DATA_FILE):
        print(f"{CLR_RED}Error: portfolio_data.json not found! Please run init_portfolio.py or restore it.{CLR_RESET}")
        sys.exit(1)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def draw_header(title):
    width = 65
    print(f"{CLR_BOLD}{CLR_CYAN}┌" + "─" * (width - 2) + "┐")
    print(f"│ {title.center(width - 4)} │")
    print(f"└" + "─" * (width - 2) + "┘{CLR_RESET}")

def draw_progress_bar(completed, total):
    width = 30
    percent = completed / total
    filled = int(width * percent)
    bar = "█" * filled + "░" * (width - filled)
    
    color = CLR_RED
    if percent >= 0.8:
        color = CLR_GREEN
    elif percent >= 0.4:
        color = CLR_YELLOW
        
    print(f"{CLR_BOLD}Progress: {color}[{bar}] {completed}/{total} ({percent:.1%}){CLR_RESET}\n")

def get_status_color(status):
    if status == "Completed":
        return CLR_GREEN
    elif status == "In Progress":
        return CLR_YELLOW
    return CLR_RED

def get_difficulty_color(diff):
    if diff == "Beginner":
        return CLR_GREEN
    elif diff == "Intermediate":
        return CLR_CYAN
    return CLR_RED

def sync_directories(data):
    """Scan folders and check if they contain a non-empty index.py/main.py. Updates status if found."""
    updated_count = 0
    for p in data:
        p_dir = os.path.join(WORKSPACE, p["dir_name"])
        if os.path.exists(p_dir):
            entry = p.get("entry_point", "index.py")
            entry_path = os.path.join(p_dir, entry)
            if os.path.exists(entry_path):
                size = os.path.getsize(entry_path)
                if size > 0:
                    is_boilerplate = False
                    try:
                        with open(entry_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            if "Created by Portfolio Manager" in content and "TODO: Add your logic here" in content:
                                is_boilerplate = True
                    except Exception:
                        pass
                    
                    if is_boilerplate:
                        if p["status"] == "Not Started":
                            p["status"] = "In Progress"
                            updated_count += 1
                    else:
                        if p["status"] in ["Not Started", "In Progress"] and size > 200:
                            p["status"] = "Completed"
                            updated_count += 1
    if updated_count > 0:
        save_data(data)
        print(f"{CLR_GREEN}Sync complete! Auto-detected and updated {updated_count} projects.{CLR_RESET}")
    else:
        print(f"{CLR_BLUE}Sync complete! All project statuses match files on disk.{CLR_RESET}")
    input("\nPress Enter to continue...")

def scaffold_project(project):
    """Create directory and boilerplate index.py for the project."""
    p_dir = os.path.join(WORKSPACE, project["dir_name"])
    os.makedirs(p_dir, exist_ok=True)
    
    entry_file = project.get("entry_point", "index.py")
    file_path = os.path.join(p_dir, entry_file)
    
    # Check if the file is empty or missing
    if not os.path.exists(file_path) or os.path.getsize(file_path) < 10:
        boilerplate = f'''"""
Project: {project["name"]}
Category: {project["category"]}
Difficulty: {project["difficulty"]}
Description: {project["description"]}

Created by Portfolio Manager
"""

def main():
    print("=" * 60)
    print(f"Welcome to {project["name"]}!")
    print("=" * 60)
    print("Implement your project code inside this main() function.")
    print("=" * 60)
    # TODO: Add your logic here
    
    input("\\nPress Enter to exit...")

if __name__ == "__main__":
    main()
'''
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(boilerplate)
        print(f"{CLR_GREEN}Created boilerplate: {CLR_BOLD}{entry_file}{CLR_RESET} in folder {CLR_BOLD}{project['dir_name']}{CLR_RESET}")
    else:
        print(f"{CLR_YELLOW}File {entry_file} already exists and contains code. Skipping boilerplate creation.{CLR_RESET}")

def run_project(project):
    """Run the selected project in a subprocess."""
    p_dir = os.path.join(WORKSPACE, project["dir_name"])
    entry_file = project.get("entry_point", "index.py")
    file_path = os.path.join(p_dir, entry_file)
    
    if not os.path.exists(file_path):
        print(f"{CLR_RED}Error: File {entry_file} not found. Please start/scaffold the project first.{CLR_RESET}")
        input("\nPress Enter to continue...")
        return
        
    clear_screen()
    draw_header(f"Running: {project['name']}")
    print(f"{CLR_BLUE}Executing: python \"{file_path}\"\n{CLR_RESET}")
    print("-" * 65)
    
    try:
        # Run project and inherit terminal inputs/outputs
        result = subprocess.run([sys.executable, file_path], cwd=p_dir)
        print("\n" + "-" * 65)
        print(f"{CLR_GREEN}Project finished with exit code {result.returncode}.{CLR_RESET}")
    except Exception as e:
        print(f"\n{CLR_RED}Execution failed: {e}{CLR_RESET}")
        
    input("\nPress Enter to return to the menu...")

def project_detail_menu(project, data):
    while True:
        clear_screen()
        draw_header(f"Project Detail: {project['name']}")
        
        status_col = get_status_color(project["status"])
        diff_col = get_difficulty_color(project["difficulty"])
        
        print(f"{CLR_BOLD}Name:         {CLR_RESET}{project['name']}")
        print(f"{CLR_BOLD}Category:     {CLR_RESET}{project['category']}")
        print(f"{CLR_BOLD}Difficulty:   {diff_col}{project['difficulty']}{CLR_RESET}")
        print(f"{CLR_BOLD}Status:       {status_col}{project['status']}{CLR_RESET}")
        print(f"{CLR_BOLD}Directory:    {CLR_RESET}{project['dir_name']}")
        print(f"{CLR_BOLD}Entry Point:  {CLR_RESET}{project['entry_point']}")
        print(f"{CLR_BOLD}Description:  {CLR_RESET}{project['description']}\n")
        
        print(f"{CLR_BOLD}Actions:{CLR_RESET}")
        print(f" 1. Start / Scaffold Project {CLR_YELLOW}(Set to 'In Progress' & create boilerplate){CLR_RESET}")
        print(f" 2. Run Project {CLR_GREEN}(Launch in terminal){CLR_RESET}")
        print(f" 3. Mark Status manually")
        print(f" 4. Back to list")
        
        choice = input("\nSelect an action (1-4): ").strip()
        
        if choice == "1":
            project["status"] = "In Progress"
            save_data(data)
            scaffold_project(project)
            input("\nPress Enter to continue...")
        elif choice == "2":
            run_project(project)
        elif choice == "3":
            print("\nSelect new status:")
            print(" 1. Not Started")
            print(" 2. In Progress")
            print(" 3. Completed")
            status_choice = input("Choice (1-3): ").strip()
            if status_choice == "1":
                project["status"] = "Not Started"
            elif status_choice == "2":
                project["status"] = "In Progress"
            elif status_choice == "3":
                project["status"] = "Completed"
            save_data(data)
            print(f"{CLR_GREEN}Status updated to '{project['status']}'!{CLR_RESET}")
            input("\nPress Enter to continue...")
        elif choice == "4":
            break

def list_projects_menu(data, filter_func=None, title="All Projects"):
    page_size = 15
    current_page = 0
    
    while True:
        filtered_list = [p for p in data if filter_func(p)] if filter_func else data
        total_projects = len(filtered_list)
        total_pages = max(1, (total_projects + page_size - 1) // page_size)
        
        if current_page >= total_pages:
            current_page = total_pages - 1
            
        clear_screen()
        draw_header(f"{title} (Page {current_page + 1}/{total_pages})")
        
        start_idx = current_page * page_size
        end_idx = min(start_idx + page_size, total_projects)
        
        print(f"{CLR_BOLD}{'ID':<4} {'Project Name':<45} {'Difficulty':<15} {'Status':<15}{CLR_RESET}")
        print("─" * 80)
        
        for idx in range(start_idx, end_idx):
            project = filtered_list[idx]
            status_col = get_status_color(project["status"])
            diff_col = get_difficulty_color(project["difficulty"])
            
            # Show simplified display index
            display_id = idx + 1
            name_truncated = project["name"][:42] + "..." if len(project["name"]) > 45 else project["name"]
            
            print(f"{display_id:<4} {name_truncated:<45} {diff_col}{project['difficulty']:<15}{status_col}{project['status']:<15}{CLR_RESET}")
            
        print("─" * 80)
        print(f"{CLR_BOLD}Navigation:{CLR_RESET} [n] Next Page  [p] Prev Page  [ID] View Details  [q] Back to Main Menu")
        
        nav = input("\nEnter choice: ").strip().lower()
        
        if nav == "n":
            if current_page < total_pages - 1:
                current_page += 1
        elif nav == "p":
            if current_page > 0:
                current_page -= 1
        elif nav == "q":
            break
        elif nav.isdigit():
            idx = int(nav) - 1
            if 0 <= idx < total_projects:
                project_detail_menu(filtered_list[idx], data)
            else:
                print(f"{CLR_RED}Invalid ID.{CLR_RESET}")
                input("\nPress Enter to continue...")

def main_menu():
    data = load_data()
    
    while True:
        clear_screen()
        draw_header("100 PYTHON PROJECTS PORTFOLIO")
        
        completed = sum(1 for p in data if p["status"] == "Completed")
        in_progress = sum(1 for p in data if p["status"] == "In Progress")
        not_started = sum(1 for p in data if p["status"] == "Not Started")
        total = len(data)
        
        draw_progress_bar(completed, total)
        
        print(f" {CLR_BOLD}Status Summary:{CLR_RESET}")
        print(f"   🟢 Completed:   {CLR_GREEN}{completed}{CLR_RESET}")
        print(f"   🟡 In Progress: {CLR_YELLOW}{in_progress}{CLR_RESET}")
        print(f"   🔴 Not Started: {CLR_RED}{not_started}{CLR_RESET}\n")
        
        print(f" {CLR_BOLD}Menu Options:{CLR_RESET}")
        print("   1. List All Projects")
        print("   2. Filter by Category")
        print("   3. Filter by Difficulty")
        print("   4. Filter by Status")
        print("   5. Search Projects by Keyword")
        print("   6. Sync Folders (Auto-Detect Completed Projects)")
        print("   7. Exit")
        
        choice = input("\nSelect an option (1-7): ").strip()
        
        if choice == "1":
            list_projects_menu(data, None, "All Projects")
        elif choice == "2":
            categories = sorted(list(set(p["category"] for p in data)))
            print("\nSelect a Category:")
            for i, cat in enumerate(categories, 1):
                print(f"  {i}. {cat}")
            cat_choice = input("\nChoice (1-{}): ".format(len(categories))).strip()
            if cat_choice.isdigit():
                c_idx = int(cat_choice) - 1
                if 0 <= c_idx < len(categories):
                    cat_name = categories[c_idx]
                    list_projects_menu(data, lambda p: p["category"] == cat_name, f"Category: {cat_name}")
        elif choice == "3":
            difficulties = ["Beginner", "Intermediate", "Advanced"]
            print("\nSelect Difficulty:")
            for i, diff in enumerate(difficulties, 1):
                print(f"  {i}. {diff}")
            diff_choice = input("\nChoice (1-3): ").strip()
            if diff_choice == "1":
                list_projects_menu(data, lambda p: p["difficulty"] == "Beginner", "Beginner Projects")
            elif diff_choice == "2":
                list_projects_menu(data, lambda p: p["difficulty"] == "Intermediate", "Intermediate Projects")
            elif diff_choice == "3":
                list_projects_menu(data, lambda p: p["difficulty"] == "Advanced", "Advanced Projects")
        elif choice == "4":
            print("\nSelect Status:")
            print("  1. Completed")
            print("  2. In Progress")
            print("  3. Not Started")
            status_choice = input("\nChoice (1-3): ").strip()
            if status_choice == "1":
                list_projects_menu(data, lambda p: p["status"] == "Completed", "Completed Projects")
            elif status_choice == "2":
                list_projects_menu(data, lambda p: p["status"] == "In Progress", "In Progress Projects")
            elif status_choice == "3":
                list_projects_menu(data, lambda p: p["status"] == "Not Started", "Not Started Projects")
        elif choice == "5":
            keyword = input("\nEnter search keyword: ").strip().lower()
            list_projects_menu(data, lambda p: keyword in p["name"].lower() or keyword in p["description"].lower(), f"Search Results for '{keyword}'")
        elif choice == "6":
            clear_screen()
            draw_header("Syncing Files with Database")
            sync_directories(data)
        elif choice == "7":
            print(f"\n{CLR_GREEN}Happy coding! Keep building your portfolio.{CLR_RESET}")
            break

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{CLR_GREEN}Goodbye!{CLR_RESET}")
        sys.exit(0)
