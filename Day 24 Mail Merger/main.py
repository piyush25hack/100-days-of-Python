replacer = "[name]"

# 1. Saare naam read karo
with open("Day 24 Mail Merger/Input/Names/invited_names.txt") as file:
    names = file.readlines()
   
# 2. Starting letter (.txt) ka text read karo
with open("Day 24 Mail Merger/Input/Letters/starting_letter.txt") as pro:
    b = pro.read()
    
    # 3. Yeh loop har ek naam ke liye chalega
    for name in names:
        stripped_name = name.strip()
        new_letter = b.replace(replacer, stripped_name)
        print(new_letter)
        
        # Sahi Tarika: Yeh block ab FOR LOOP KE ANDAR hai (four spaces indented)
        # Isse har ek bande ka alag .txt file save hoga!
        with open(f"Day 24 Mail Merger/Output/ReadyToSend/Letter_for_{stripped_name}.txt", mode="w") as completed:
            completed.write(new_letter)