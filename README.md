# THE BEGINNINGS 

Welcome LADIES AND GENTLEMAN,
There are few projects which i would like to desribe:
                                                                           First one "bot na openBB"
1. Streamlit App (Stock News Sentiment Tracker)
Components:
Streamlit App Setup:

The app is created using the Streamlit library.
It uses the openbb_terminal SDK to fetch financial news sentiment and related information.
User Input:

Users can input a stock ticker in a text input field.
Functionality:

The get_news_signal function is defined to retrieve the latest news article for the provided stock ticker.
The sentiment of the news article is then analyzed using the openbb SDK's text_sent function.
Depending on the sentiment score, the app displays a recommendation to buy, sell, or states that there's no useful signal.
The app also provides a link to the latest news article.
Workflow:
User inputs a stock ticker.
The app fetches the latest news article for that stock using the openbb.stocks.ba.cnews function.
The sentiment of the news article is analyzed using the openbb.stocks.ba.text_sent function.
The app displays a recommendation based on the sentiment score and provides a link to the news article.
2. Dash App (PCA on Stock Returns)
Components:
Dash App Setup:

The app is created using the Dash library with Bootstrap styling.
It also uses the openbb_terminal SDK for financial data retrieval.
User Input:

Users can input a list of stock tickers, choose the number of principal components for PCA, and select a date range.
Functionality:

The app performs Principal Component Analysis (PCA) on the daily returns of the selected stocks.
It displays two graphs: a bar chart showing the explained variance by each principal component and a line chart showing the cumulative explained variance.
Workflow:
User inputs a list of stock tickers, selects the number of principal components, and chooses a date range.
On clicking the "Submit" button, the app fetches historical stock data for the specified tickers and date range using openbb.economy.index.
Daily returns are calculated, and PCA is applied using the sklearn.decomposition.PCA module.
The app generates two graphs - a bar chart showing explained variance by each component and a line chart showing cumulative explained variance.

                                                                                                        
                                                                                                        
# second one "catsystem3

Its a basic implementation of api and using typical Methods like delete,post,get to get,send or delte a cat which conatins id,url,data etc 
MORE INFO WILL BE SOON PROVIDED

# Cwiczenia.py 
ChessGame Class:

The ChessGame class represents the state and logic of a simple chess game.
It has an __init__ method that initializes the chessboard with the starting position of pieces and sets the current player to 'white'.
The print_board method prints the current state of the chessboard.
The is_valid_move method checks whether a move from the specified starting position to the ending position is valid. It currently allows any non-capturing move, and it checks if the piece belongs to the current player.
The play method is the main game loop. It continuously prints the board, prompts the current player for a move, and updates the board if the move is valid.
Chessboard Representation:

The chessboard is represented as a list of lists (self.board). Each sublist represents a row, and each element within the sublist represents a square on the chessboard. Pieces are represented by single characters: 'P' for pawn, 'R' for rook, 'N' for knight, 'B' for bishop, 'Q' for queen, and 'K' for king. Lowercase letters represent black pieces, and uppercase letters represent white pieces.
Game Execution:

The script creates an instance of the ChessGame class (game = ChessGame()) and starts the game by calling the play method (game.play()).
User Interaction:

During each turn, the current state of the chessboard is printed, and the player is prompted to enter the starting and ending positions for their move.
Move Execution:

If the entered move is valid (according to the basic rules in the is_valid_move method), the board is updated, and the current player is switched for the next turn.
If the move is not valid, an error message is displayed, and the player is prompted to try again.
Game Loop:

The game continues in a loop, allowing players to take turns until interrupted externally (e.g., manually stopping the script).

!!It's worth noting that the current code provides a basic framework for a chess game but lacks specific rules for different pieces' movements and capturing. 

# game 
Enum Definitions:
game_prob: Enum representing possible outcomes of the first roll - "Chest" or "Empty."
Colours: Enum representing different chest colors - Green, Orange, Purple, and Gold.
Probability Distributions:

first_roll: Dictionary mapping the outcomes of the first roll to their probabilities.
chestColoursDictionary: Dictionary mapping chest colors to their probabilities for the second roll.
gold_reward: Dictionary calculating gold rewards based on the chest colors.
Game Mechanics:

The game has a fixed length (game_length set to 5).
Player is prompted to move forward ("Yes" or any case variation) in a loop.
For each move:
A random outcome (game_event) is determined for the first roll.
If a chest is obtained:
A chest color is randomly chosen for the second roll.
Gold reward is calculated based on the chosen color using the gold_reward dictionary.
A random gold gain within a certain percentage range is calculated using gain_gold_approx function.
The total gold (gold_aqq) is updated, and the result is printed.
If no chest is obtained, a message is printed indicating no reward.
The loop continues until the game_length reaches 0.

Utility Functions:
gain_gold_approx: A function to calculate a random gold value within a given percentage range.

Print Statements:
Various print statements provide information about the game's progress and outcomes.
