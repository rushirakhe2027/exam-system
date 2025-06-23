with open('app/routes/student.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix line 611 (index 610) - misplaced else
lines[610] = '                else:\n'

# Fix line 613 (index 612) - print statement indentation  
lines[612] = '                    print(f"Failed to process question data: {q_data}")\n'

# Fix line 632 (index 631) - session.pop indentation
lines[631] = '        session.pop(f"exam_{exam_id}_answers", None)\n'

with open('app/routes/student.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Fixed all indentation issues') 