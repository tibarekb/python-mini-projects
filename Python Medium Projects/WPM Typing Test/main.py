import curses 
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!") # 1 line down, 0 character from the right
    stdscr.addstr(1, 0, "Press any key to begin!") # 1 line down, 0 character from the right
    stdscr.refresh()
    stdscr.getkey()
    
def display_text(stdscr, target, current, wpm=0)
    
def wpm_test(stdscr):
    target_text = "Hello world this is some test text for this app!"
    current_text = []
    
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    
    while True:
        stdscr.clear()
        stdscr.addstr(target_text)
        
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
            
        stdscr.refresh()
        
        key = stdscr.getkey()
        if ord(key) == 27:
            break
        
          
        current_text.append(key)
        
       
        
       
    
    
    
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    wpm_test(stdscr)
    
    
wrapper(main)