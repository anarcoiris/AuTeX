# First things first: Apologies for the (lack of!) order. The code is in constant change and will clean the mess when all the functions are doing fine

# AuTeX
 Automated LaTeX formatting tool = Helper to get big chunks of chapter&text into latex, saving +2.000 "\newline" "\chapter" "\newpage" and other annoying things.
  1) You need to run the textChain function
  2) I advise running first "import autex" from the python shell
  3) Then you can do autex.textChain('filename.docx') - dont forget about the extension
  4) It will yield a couple of .txt file with json format. The filename.tex will be ordered key[i] = chapter[i]; key2[i]= paragraphs of the body text
  5) It performs a simple latex formating consisting of \newlines each new paragraph and \newpage \chapter in front of every chapter
  6) %TO DO: import the strings to a .tex template file, add input to choose document class - hence different template use


# Guitarmaster
Automated music modes&scales calculator - Beginner learning tools
 1) just do "python guitarmaster.py" to run the script.
 2) When asked for, input first the key (A, As, B, C, Cs...) and then the mode "jonico","dorico","Lidio","Eolico","Mixo"...
 3) You can just spam 0 + enter to get all the action cycle over your setup.
 4) %TO DO: Add the rest of the modes. Add a chord construction for each modal progression and a chord type identifier.
 5) %longterm: modes and tones correlation for modulation as well as modulation chains and routes between tone/mode grades.
