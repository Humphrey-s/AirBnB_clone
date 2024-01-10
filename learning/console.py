#!/usr/bin/env python3
import cmd


class HelloWorld(cmd.Cmd):

    def do_greet(self, line):

        if len(line) == 0:
            print("Hello Everyone")
        else:
            print("Hello {}".format(line))

    def do_EOF(self, line):
        return True

if __name__ == "__main__":
    HelloWorld().cmdloop()
