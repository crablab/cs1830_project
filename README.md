# cs1830

Ideas board: https://docs.google.com/document/d/1_0hMUYIG_HRFGZmB0RdLcXk4QeVVlYxAIiLZAO06mQw/edit?usp=sharing

SETTINGS: located in classes/

PROJECT STRUCTURE:

CS1830/                                                # main project Files
    .gitignore
    GameLoop.py
    lisence
    packages
    readme.md

    CLASSES/
        config.py
        settings.py

       BASE/                                           # Base classes which are used everywhere
            vectors.py/

       MIDDLE/                                         # all Middle classes that are used in Super and inherit Base
            Particle.py

            SPRITECONTROL/
                SpriteAnimator.py
                spriteSheet.py

       SUPER/                                          # all Super classes that inherit Middle and Base
            Camera.py
            Monster.py
            MonsterAi.py
            Player.py
            Weapon.py

    GAMESTATES/
        GameStates.py
        intro.py

    HANDLERS/                                           # event related detection
        ClickHandler.py
        KeyHandler.py
        Mouse.py

    IMG/
        all img assests in named directories

    LOADING/                                            # any generation of objects to in game
        MonsterAi.py
        Objects.py
        RandomGen.py

    TRANSFER/                                           # Network related
        comms.py
        JsonToObject.py

