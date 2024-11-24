import os

# List of Python files
python_files = [
    '6_10_current.py', 'ACSL_Binary_counting_Hard.py', 'ACSL_Contest_3_code.py', 'ACSL_Lights_Out.py',
    'Bits.py', 'BlackJack_Final.py', 'bubble_sorting.py', 'Ceasar_cypher.py', 'Chaos_game_pt3.py',
    'Chapter_3_26.py', 'Chess_king_positions.py', 'Contest_2_Senior_division.py', 'Digit_Differentation.py',
    'Fiboacci_and_pascal.py', 'FIxed_Chess_king_postions.py', 'Fractions.py', 'Insertion_sorting.py',
    'memorization.py', 'Ninety_NIne.py', 'Pascals_triangle_recursion_test.py', 'Pete_s_Paint.py',
    'Pete_s_Paint_graphics.py', 'Recursion_pt2.py', 'Recursive_functions_AP (1).py', 'Recursive_functions_AP.py',
    'Schweigert_s_Shoulder.py', 'Searching_pt2.py', 'Selection_Sorting.py', 'Spelling_Bee.py',
    'Spelling_Bee_(final).py', 'String_mutulation.py', 'Student_and_Course_Class.py',
    'TeamAlexProblem1.python.py', 'TeamAlexProblem2.python.py', 'TeamAlexProblem3.python.py',
    'TeamAlexProblem4.python.py', 'TeamAlexProblem5.python.py', 'TeamAlexProblem6.python.py',
    'TeamAlexProblem7.python.py', 'Team_AlexProblem9.python.py', 'Toothpick_Game.py',
    'Toothpick_Game_pt3.py', 'Tower_Defense_Project.py', 'Tower_of_Hanoi_Code.py', 'WDTPD.py',
    'We_Try_even_Harder.py', 'Wordle.py', 'Wordle_backup.py', 'Working_code_HackerRank.py'
]

# Base GitHub URL
github_base_url = "https://github.com/AlexSeisler/Python-Codes/blob/main/PythonCodes/"

# Function to generate a description based on the filename
def generate_description(filename):
    if "sort" in filename.lower():
        return "A Python implementation of a sorting algorithm."
    elif "recursion" in filename.lower():
        return "A project demonstrating recursive functions in Python."
    elif "game" in filename.lower():
        return "A Python game development project."
    elif "paint" in filename.lower():
        return "A drawing application created using Python."
    elif "wordle" in filename.lower():
        return "A Python recreation of the popular Wordle game."
    elif "chess" in filename.lower():
        return "A project exploring chess logic or moves."
    elif "tower" in filename.lower():
        return "A Python implementation of the Tower of Hanoi or similar challenge."
    elif "binary" in filename.lower():
        return "A project involving binary operations or counting."
    else:
        return "A Python project exploring interesting concepts."

# Generate HTML for the projects
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Projects Timeline</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="header">
        <h1>Python Projects Showcase</h1>
    </header>
    <div class="timeline">
"""

# Create cards in rows (2 per row for better organization)
for i, filename in enumerate(python_files):
    if i % 2 == 0:
        html_content += '<div class="timeline-row">\n'  # Start a new row
    
    # Generate the card
    project_name = filename.replace(".py", "").replace("_", " ").title()
    description = generate_description(filename)
    github_link = github_base_url + filename
    html_content += f"""
        <div class="timeline-card">
            <div class="card-content">
                <h3>{project_name}</h3>
                <p>{description}</p>
                <a href="{github_link}" target="_blank" class="github-link">View on GitHub</a>
            </div>
        </div>
    """
    
    if i % 2 == 1 or i == len(python_files) - 1:
        html_content += '</div>\n'  # Close the row

# Close the HTML structure
html_content += """
    </div>
</body>
</html>
"""

# Save the HTML content to a file
output_file = "python_projects_timeline.html"
with open(output_file, "w") as file:
    file.write(html_content)

print(f"HTML file generated: {output_file}")