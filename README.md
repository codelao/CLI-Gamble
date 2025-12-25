<h1 align="center">
    CLI Gamble
</h1>
<p align="center">
    Welcome to my first project since 2023! Was a bit tired of vibecoding and focused on my studies instead.</br>
    "CLI Gamble" is a simple casino simulator that works directly in your computer's terminal. I wrote it when I was out of internet during my trip to Cuba.</br>
    <h3>Disclaimer!</h3>This game doesn't involve the use of real money. All "gambling" process is virtual and you're not supposed to change it except the virtual game parameters such as start-up funds and chance of winning.
</p>

* [Installation](#installation)
* [Configuring game parameters](#configuring-game-parameters)
* [Game screenshots](#screenshots)

## How it works
##### After installing, open your command line and enter this `casino` to start the game.</br>I've added some virtual "funds" to your account by default so you don't need to configure anything if you are satisfied with my default parameters, but if you want, you can proceed to [Configuring game parameters](#configuring-game-parameters) section.</br>Then you just choose your bet size and hit Enter to spin and test your luck.</br>You can hit either standard or big win, free bets, or jackpot. Your win size partially depend on your bet size and general win multiplier too *(note that given multipliers won't work when you win something during the free bet)*.</br>Good luck!

## Installation 
### macOS/Linux:
#### 1. Download [install.sh](https://github.com/codelao/CLI-Gamble/releases) file from the latest release.
#### 2. Run this file:
```
bash install.sh
```
#### 3. Re-open your terminal and run `gamble`. If the game started, you're all set.

**Note for install script output "*Unknown rc file!*"**
If the install script didn't work for your system, you would need to manually follow its logic based on your run control file type (it is usually still about just adding this line inside your rc)
```
alias gamble="python3 ~/CLI-Gamble/game/gamble.py"
```

### Windows:
#### 1. Download [install.bat](https://github.com/codelao/CLI-Gamble/releases) file from the latest release.
#### 2. Run this file:
```
install
```
#### 3. Re-open your terminal and run `gamble`. If the game started, you're all set.

## Configuring game parameters
### Changing your initial deposit and amount of free bets:
##### [wallet.csv](https://github.com/codelao/CLI-Gamble/blob/main/game/wallet.csv) contains two values on second line: first - your deposit, second - free bets. You can change this parameters either in a text editor or in specialized programs like Microsoft Excel.
### Changing general win multiplier and win chances:
##### [casino.py](https://github.com/codelao/CLI-Gamble/blob/main/game/casino.py) is a main game script where on lines *14, 20, 21, 22, 23* you can set your own win chances and multipliers (hints are provided inside the script).


## Screenshots
<img src="https://i.imgur.com/rc0Q8Hx.png" width="85%">
<img src="https://i.imgur.com/kNdyoPr.png" width="85%"></br>
<img src="https://i.imgur.com/zyzjCeG.png" width="50%">
