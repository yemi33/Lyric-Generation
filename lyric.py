from engine import GrammarEngine

def lyric():
    engine = GrammarEngine(file_path="grammars/lyric.txt")
    for i in range(1):
      output = engine.generate(start_symbol_name="lyrics", debug=False) 
      output_list = output.split("\\n")
      for i in range(len(output_list)):
        print(f"{output_list[i]}")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Lyric -- ")
    lyric()
