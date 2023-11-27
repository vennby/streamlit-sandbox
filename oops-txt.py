import streamlit as lit
from streamlit_metrics import metric, metric_row
from streamlit_ace import st_ace as lit_ace

import os
import subprocess

import pandas as pd
import numpy as np
import altair as alt
import cufflinks as cf

lit.set_page_config(
    page_title="Object-Oriented Design and Patterns",
    page_icon=":computer:",
    layout="wide",
)

pages = {'Chapter 1': 'Chapter 1', 'Chapter 2': 'Chapter 2', 'Chapter 3': 'Chapter 3',
         'Chapter 4': 'Chapter 4', 'Chapter 5': 'Chapter 5', 'Chapter 6': 'Chapter 6',
         'Chapter 7': 'Chapter 7', 'Chapter 8': 'Chapter 8', 'Chapter 9': 'Chapter 9',
         'Chapter 10': 'Chapter 10'}

for page_name, page_title in pages.items():
    if lit.sidebar.button(page_title, key=page_name):
        lit.session_state.page = page_name

page = getattr(lit.session_state, "page", list(pages.keys())[0])

lit.title('Chapter 1: A Crash Course in Java')
markdown_content = """
# Classes, Objects, and Constructors

Here's a simple program in Java, with a single **class** "Greeter". The file with this program should be saved as "Greeter.java" (i.e. the name of the class with the main method in it) to be compiled and interpreted.
``` java
public class Greeter // class name
{
  private String name; //instance variable of private type

  public Greeter(String aName) //constructor
  {
    name = aName; // initialization of the form "instance variable = input parameter"
  }

  public String sayHello() //sample String function in a class, also called a "method"
  {
    return "Hello, " + name + "!";
  }

  public static void main(String[] args) //the main method
  {
    Greeter venn = new Greeter("Vennela"); //an object venn of Greeter class is created
    System.out.println(venn.sayHello()); //the method sayHello() is invoked
  }
}
```
The class *Greeter* has the following features:-
1. A class member <br>
   In this program, "name" is a **field**, or a member of the class "Greeter".
2. A constructor <br>
   Everything contained within "public Greeter(String aName)" is a part of the **constructor**.
3. A method <br>
   *sayHello()* is an example of a typical **method** in a class.
4. A main method <br>
   Everything contained within "public static void main(String[] args)" is a part of the **main method**.

An **object** is an instance of a class, with all of the fields and methods of the class in it. It is used to invoke the methods in a non-static class.
Here, *venn* is an object of type **Greeter**. It is declared using the **new** keyword.

The program can also look like this, **without** a constructor:
```java
public class Greeter
{
    public String sayHello(String name)
    {
        return "Hello, " + name + "!"; 
    }
    
    public static void main(String args[]) 
    {
        Greeter venn = new Greeter();
        System.out.println(venn.sayHello("venn"));
    }
    
    private String name;
}
```
In this case, there is a **default constructor** set into place. The default constructor:-
1. Doesn't accept any parameters
2. Is provided automatically by the Java compiler
3. Initialises instance variables to default values

# 'Static' Keyword

**Static** is a keyword that is used to define class-level member(variable or method) rather than an instance variable.
Static class members can be accessed without the creation of an object of the class.
There will be only one copy of a static variable shared among all instances of the class, it is created when the class is loaded and exists for the lifetime of the program.

Here is the same program, but there is no requirement to create an object to call the *sayHello()* method of the class, since it is a **static** method.
```java
public class Greeter
{
    public static String sayHello(String name)
    {
        return "Hello, " + name + "!"; 
    }
    
    public static void main(String args[]) 
    {
        System.out.println(sayHello("venn"));
    }
    
    private String name;
}
```
"""

lit.markdown(markdown_content)

lit.title("Try it Yourself!")

THEMES = [
    "ambiance",
    "chaos",
    "chrome",
    "clouds",
    "clouds_midnight",
    "cobalt",
    "crimson_editor",
    "dawn",
    "dracula",
    "dreamweaver",
    "eclipse",
    "github",
    "gob",
    "gruvbox",
    "idle_fingers",
    "iplastic",
    "katzenmilch",
    "kr_theme",
    "kuroir",
    "merbivore",
    "merbivore_soft",
    "mono_industrial",
    "monokai",
    "nord_dark",
    "pastel_on_dark",
    "solarized_dark",
    "solarized_light",
    "sqlserver",
    "terminal",
    "textmate",
    "tomorrow",
    "tomorrow_night",
    "tomorrow_night_blue",
    "tomorrow_night_bright",
    "tomorrow_night_eighties",
    "twilight",
    "vibrant_ink",
    "xcode",
]

KEYBINDINGS = ["emacs", "sublime", "vim", "vscode"]

editor, executor = lit.tabs(["Editor", "Executor"])

INITIAL_CODE = """
class Main
{
    public static void main(String[] args)
    {
        System.out.println("Hello World!");
    }
}        
"""
with editor:
    code = lit_ace(
        value=INITIAL_CODE,
        language="Java",
        placeholder="// Enter code here",
        theme="twilight",
        keybinding="vscode",
        show_gutter=True,
        show_print_margin=True,
        auto_update=False,
        readonly=False,
        key="ace-editor",
    )
    lit.write("Hit `CTRL+ENTER` to refresh")
    lit.write("*Remember to save your code separately!*")

with executor:
    with open("Main.java", "w") as file:
        file.write(code)
    compile_process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    compile_output, compile_error = compile_process.communicate()

    if compile_process.returncode == 0:
        run_process = subprocess.Popen(["java", "Main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        run_output, run_error = run_process.communicate()

        lit.code(f"Compile Output:\n{compile_output.decode()}\n\nRun Output:\n{run_output.decode()}")
    else:
        lit.code(f"Compile Error:\n{compile_error.decode()}")
