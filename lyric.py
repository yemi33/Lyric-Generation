from engine import GrammarEngine

def lyric():
    engine = GrammarEngine(file_path="grammars/lyric.txt")
    for i in range(1):
      output = engine.generate(start_symbol_name="lyrics", debug=False) 
      output_list = output.split("\\n")
      for i in range(len(output_list)):
        print(f"{output_list[i]}")


def generate_lyric():
    """The function that generates the lyrics."""
    print("\n\n-- Lyric -- ")
    lyric()
