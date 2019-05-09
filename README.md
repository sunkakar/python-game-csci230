# GUI Text-based RPG Game in Python


## *Overview*

- I programmed a text-based role playing game. The game is called “Hunt for King Rebet.” It goes along a story which is played in a 3-choice interface where one can choose from 3 choices and affect the flow of the game. An old text-based RPG inspires the game, “ZORK”, however I have programmed the game completely using GUI giving ease to the u`ser.

## *Requirements*

-   The game is programmed completely in Python.

-   It uses class data structure.

-   It incorporates Graphics User Interface using Tkinter module

-   It converts a simple text based RPG which is played by typing in
    your choice. It sometimes can be difficult for a new user to
    understand and remember all possible inputs. Translating that into a
    GUI environment, the user finds ease using Buttons and reading
    Labels.

-   The game doesn’t crash under typical load if played correctly. The
    only thing the user needs to do is press the button next to his
    choice and then click continue button twice.

-   The program illustrates object oriented programming by the use of
    global and local variables throughout all the functions used in the
    class. The program has been attempted to be as simple as possible
    making it easy for a third person to understand its working on
    reading.

-   This is completely made from scratch by me.

## *Data Plan*

-   The overall data structure of the game is like many Tkinter
    programs. It’s all built in a class enclosing multiple functions.

- [![Image from Gyazo](https://i.gyazo.com/fc929a1e251008d7bdab3f8cb0a173f3.png)](https://gyazo.com/fc929a1e251008d7bdab3f8cb0a173f3)

-   The main Tk GUI Window looks like this:

- [![Image from Gyazo](https://i.gyazo.com/64ba4af79116adeeba2c339f2c1994ef.png)](https://gyazo.com/64ba4af79116adeeba2c339f2c1994ef)

    The data that is being manipulated are:

    -   Labels 1 and 2: These labels tell the story and are updated
        every time the user makes a choice and clicks continue. This way
        the storyboard of the game moves on in the direction the user
        takes it with his choices.

    -   Button 1: The Continue button is updated every time the user
        makes a choice. Once the user makes a choice the button is
        updated to jump to the corresponding function with that choice.
        The continue button disappears when the game ends stopping the
        user from giving any further inputs.

    -   Radio Buttons: These buttons are updated every time the user
        makes a choice to give new options as the story progresses. The
        text variable or the text value is updated. These buttons are
        also deselected after every time the game moves on from a user
        input. This is done so that the value of the button doesn’t go
        through the next function.

    -   Label 3: Label 3 changes to the Win/Loss status of the game when
        the game comes to an end.

- [![Image from Gyazo](https://i.gyazo.com/fd262a2ad6b3151685de35c25a3da48e.png)](https://gyazo.com/fd262a2ad6b3151685de35c25a3da48e)

-   The game has a sophisticated layout. The storyboard branches out
    giving the user different choices of how the story progresses. All
    the choices made lead to a final boss fight. The sub-choices can
    lead you back so the user can go back and choice differently if
    needed. Every choice has its own different function. Since the
    functions are all separate they could lead to any function in the
    program. For instance, Choice 3 -&gt; Choice 3.1 -&gt; Choice 2.

- [![Image from Gyazo](https://i.gyazo.com/d54c8a100199abd48365acbda9ce155d.png)](https://gyazo.com/d54c8a100199abd48365acbda9ce155d)

## *Visual Layout*

-   The following is the visual layout of all the widgets in the tk
    window using grid() method.

    [![Image from Gyazo](https://i.gyazo.com/4bbb8af76cc65beb13e7eb377ecc109f.png)](https://gyazo.com/4bbb8af76cc65beb13e7eb377ecc109f)


-   The screens have the same basic layout as above.

    [![Image from Gyazo](https://i.gyazo.com/bc526da15fbf9cd27454faf266308738.png)](https://gyazo.com/bc526da15fbf9cd27454faf266308738)

    [![Image from Gyazo](https://i.gyazo.com/f092720941f169073fc80b53ab79cb20.png)](https://gyazo.com/f092720941f169073fc80b53ab79cb20)

-   When the program begins, the user sees the following window

    [![Image from Gyazo](https://i.gyazo.com/8f13ffb7939485865235047042085a87.png)](https://gyazo.com/8f13ffb7939485865235047042085a87)

    The user is introduced to the name of the game and the objective/aim.
    He/she is also told how to play. The user starts by choosing play and
    clicking Continue button. The following window will pop up.

    [![Image from Gyazo](https://i.gyazo.com/d4a04e6501733d0ffb09dd707ca747a4.png)](https://gyazo.com/d4a04e6501733d0ffb09dd707ca747a4)

    To perfectly use the option “Look around”, the user should click the
    radio button next to it and then double click Continue. This is how any
    progress will be made in the game. When the user chooses “Look around”,
    the Continue button calls function Lookaround() which updates the
    choices and the storyboard which looks like :

    [![Image from Gyazo](https://i.gyazo.com/cdde574659a85157380deef34000fc89.png)](https://gyazo.com/cdde574659a85157380deef34000fc89)

    The function Lookaround then gives 3 new options which then reference to
    a new function each. When the button is used to call a new function, the
    continue button is deleted using grid\_forget and a new button is
    created in its place that calls a new function. This way the button
    leads to a new function and doesn’t execute the current function again.

## *Storyline*

I wrote the program in its entirety by myself which includes the storyline.

