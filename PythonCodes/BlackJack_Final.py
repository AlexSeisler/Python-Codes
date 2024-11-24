Game.java:
---------
/*
This class is used to keep track of the deck and the players identity
*/
import java.util.ArrayList;
import java.util.Random;
import java.util.Collections;

public class Game 
{
    private int betAmount;
    private Player thePlayer;
    private ArrayList<String> deck;
    
    /*
    Creates a deck and the players information
    @param, A player Object, and a bet amount
    @return a Game Object
    */
    public Game(Player thePlayer, int betAmount)
    {
        this.deck = new ArrayList<>();
        this.thePlayer = thePlayer;
        this.betAmount = betAmount;
    }
    /*
    Creates a new and reshuffled deck
    @param, none
    @return, void, creates a deck variable
    */
    public void play()
    {
        
        String[] suits = {"Hearts", "Diamonds", "Clubs", "Spades"};
        String[] ranks = {"2","3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"};

        // Populate the deck
        for (String suit : suits) {
            for (String rank : ranks) {
                deck.add(rank + " of " + suit);
            }
        }

        // Shuffle the deck
        shuffle();
    }
    /*
    getter method for the betAmount variable
    @param, none
    @return, betAmount variable
    */
    public int getBetAmount()
    {
        return this.betAmount;
    }
    /*
    setter method for the betAmount variable
    @param, an integer representing the bet amount
    @return, none void sets the variable
    */
    public void setBetAmount(int amount)
    {
        this.betAmount=amount;
    }
    /*
    A shuffle method that rearranges the deck instance variable
    @param, none
    @return, none a rearagned deck
    */
    public void shuffle() 
    {
        Collections.shuffle(deck);
        
    }
    /*
    A to string for printing card objects
    @param, none
    @return, a card in string formatting
    */
    public String dealCard() 
    {
        if (deck.isEmpty()) {
            return null; // If deck is empty, return null
        }
        return deck.remove(0);
    }

        
        
    
}

MyProgram.java:
--------------
//Uses the Game and Player class, along with other methods to simulate the game of blackjack to the user. 
import java.util.ArrayList;
import java.util.Scanner;
public class MyProgram
{
    /*Simulates the game blackjack to the user using user input, and print statments
    @param, user input
    @return blackjack
    */
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Hello player what do I call you?: ");
        String name = input.nextLine();
        
        
        Player Alex = new Player(name, 100, 500);
        
        while(true)
        {
            System.out.println(Alex);
            System.out.print("Enter bet amount: ");
            int Amount = input.nextInt();
            
            if(Amount==0)
            {
                System.out.println();
                System.out.println("Have A Nice Day!");
                System.out.println();
                break;
            }
            else if(Amount>Alex.getChips()||Amount<0)
            {
                System.out.println();
                System.out.println("Insufficient Funds, try again");
                System.out.println();
                continue;
            }
            
            
            
            Game g1 = new Game(Alex, Amount);
            g1.play();
                
            ArrayList<String> Player = new ArrayList<String>();
            
            ArrayList<String> Dealer = new ArrayList<String>();
            
            int next = 0;
            
    
            //start of game
            System.out.println("--Deal Start--");
            System.out.println();
            System.out.println("--Players Hand--");
            Player.add(g1.dealCard());
            System.out.println(Player.get(0));
            
            System.out.println();
            System.out.println("--Dealers Hand--");
            Dealer.add(g1.dealCard());
            System.out.println(Dealer.get(0));
            System.out.println();
            
            System.out.println("--Players Hand--");
            Player.add(g1.dealCard());
            System.out.println(Player.get(0)+ " and "+ Player.get(1));
            System.out.println();
            
            
            
            Dealer.add(g1.dealCard());
            System.out.println("--Dealers Hand--");
            
            System.out.println(Dealer.get(0)+" and "+"Hidden");
            
            int pTotal = 0;
            int dTotal = 0;
            int AceCountP=0;
            int AceCountD=0;
            
            boolean con = true;
            String User = "Stand";
            
            pTotal += cardValue(Player.get(0));
            if(cardValue(Player.get(0))==11)
            {
                AceCountP++;
            }
            
            
            pTotal += cardValue(Player.get(1));
            if(cardValue(Player.get(1))==11)
            {
                AceCountP++;
            }
            
            dTotal += cardValue(Dealer.get(0));
            if(cardValue(Dealer.get(0))==11)
            {
                AceCountD++;
            }
            
            dTotal += cardValue(Dealer.get(1));
            if(cardValue(Dealer.get(1))==11)
            {
                AceCountD++;
            }
            
            next = next(pTotal);
            int end = 0;
            while(end==0)
            {
                System.out.println();
                if(next==0&&AceCountP==0)
                {
                    System.out.println("BUST!");
                    Alex.setChips(Alex.getChips()-g1.getBetAmount());
                    Alex.setRank(Alex.getRank()-5);
                    end=1;
                    break;
                }
                else if(next==1)
                {
                    System.out.println("BLACKJACK!");
                    Alex.setChips(Alex.getChips()+g1.getBetAmount());
                    Alex.setRank(Alex.getRank()+10);
                    end=1;
                    break;
                }
                else
                {
                    
                    if(AceCountP!=0&&pTotal>21)
                    {
                        pTotal-=10;
                        AceCountP--;
                    }
                    
                    if(con)
                    {
                        System.out.println("Whats your move? (Stand) (Hit) or (Double)");
                        User = input.nextLine();
                    }
                    if(User.equals("Hit"))
                    {
                        String hold =g1.dealCard();
                        Player.add(hold);
                        pTotal+= cardValue(hold);
                        next = next(pTotal);
                        System.out.print("Current Hand: ");
                        for(int i = 0;i<Player.size();i++)
                        {
                            System.out.print(Player.get(i)+", ");
                        }
                        System.out.println();
                    }
                    else if(User.equals("Double"))
                    {
                        String hold =g1.dealCard();
                        Player.add(hold);
                        pTotal+= cardValue(hold);
                        next = next(pTotal);
                        System.out.print("Current Hand: ");
                        for(int i = 0;i<Player.size();i++)
                        {
                            System.out.print(Player.get(i)+", ");
                        }
                        g1.setBetAmount(g1.getBetAmount()*2);
                        System.out.println();
                        System.out.println("New bet amount: "+g1.getBetAmount());
                        con=false;
                        User = "Stand";
                        
                        
                    }
                    
                    else if(User.equals("Stand"))
                    {
                        
                        
                        while(dTotal<= pTotal)
                        {
                            
                            
                            next = next(dTotal);
                            System.out.println();
                            System.out.print("Dealer: ");
                            for(int i = 0;i<Dealer.size();i++)
                            {
                                
                                System.out.print(Dealer.get(i)+", ");
                            }
                            
                            if(next==0&&AceCountD==0)
                            {
                                System.out.println("Dealer Break");
                                Alex.setChips(Alex.getChips()+g1.getBetAmount());
                                Alex.setRank(Alex.getRank()+5);
                                end=1;
                                break;
                            }
                            else if(next==0&&AceCountD!=0)
                            {
                                if(AceCountD!=0&&dTotal>21)
                                {
                                    dTotal-=10;
                                    AceCountD--;
                                }
                            }
                            else if(next==1)
                            {
                                System.out.println("Dealer Blackjack");
                                Alex.setChips(Alex.getChips()-g1.getBetAmount());
                                Alex.setRank(Alex.getRank()-5);
                                end=1;
                                break;
                            }
                            else if (dTotal> pTotal)
                            {
                                System.out.println("Dealer Wins");
                                Alex.setChips(Alex.getChips()-g1.getBetAmount());
                                Alex.setRank(Alex.getRank()-5);
                                end=1;
                                break;
                            }
                            else if(dTotal<= pTotal)
                            {
                                String hold =g1.dealCard();
                                Dealer.add(hold);
                                dTotal+= cardValue(hold);
                                
                                
                                
                            }
                            
                            
                        next = next(dTotal);   
                        }
                            if(next==0&&AceCountD==0)
                            {
                                System.out.println();
                                System.out.println("DEALER BREAK");
                                Alex.setChips(Alex.getChips()+g1.getBetAmount());
                                Alex.setRank(Alex.getRank()+5);
                                end=1;
                                System.out.println();
                                System.out.println("--Dealers Final--");
                                for(int i = 0;i<Dealer.size();i++)
                                {
                                    
                                    System.out.print(Dealer.get(i)+", ");
                                }
                                System.out.println();
                                break;
                            }
                            else if(next==0&&AceCountD!=0)
                            {
                                if(AceCountD!=0&&dTotal>21)
                                {
                                    dTotal-=10;
                                    AceCountD--;
                                }
                            }
                            else if(next==1)
                            {
                                System.out.println();
                                System.out.println("DEALER BLACKJACK");
                                Alex.setChips(Alex.getChips()-g1.getBetAmount());
                                Alex.setRank(Alex.getRank()-5);
                                System.out.println();
                                System.out.println("--Dealers Final--");
                                for(int i = 0;i<Dealer.size();i++)
                                {
                                    
                                    System.out.print(Dealer.get(i)+", ");
                                }
                                System.out.println();
                                end=1;
                                break;
                            }
                            else if (dTotal> pTotal)
                            {
                                System.out.println();
                                System.out.println("DEALER WINS");
                                Alex.setChips(Alex.getChips()-g1.getBetAmount());
                                Alex.setRank(Alex.getRank()-5);
                                System.out.println();
                                System.out.println("--Dealers Final--");
                                for(int i = 0;i<Dealer.size();i++)
                                {
                                    
                                    System.out.print(Dealer.get(i)+", ");
                                }
                                System.out.println();
                                end=1;
                                break;
                            }
                            else if(dTotal<= pTotal)
                            {
                                String hold =g1.dealCard();
                                Dealer.add(hold);
                                dTotal+= cardValue(hold);
                                
                                
                                
                            }
                            else
                            {
                                System.out.println("Help");
                            }
                        
                    }
                    
                }
            }
            System.out.println();
            System.out.println("-----END HAND-----");
            System.out.println();
        }
        

        
        
        
        
        
        
    }
    /*Takes in the constructed string of the card and finds the value paired with the String
    @param, a String of the card
    @return, the integer amount paired with the card
    */
    public static int cardValue(String card)
    {
        int AceCount = 0;
        if(card.substring(0,4).equals("Jack")|| card.substring(0,5).equals("Queen")||card.substring(0,4).equals("King")||card.substring(0,2).equals("10"))
        {
            return 10;
        }
        else if(card.substring(0,3).equals("Ace"))
        {
            AceCount++;
            return 11;
        }
        else
        {
            return Integer.valueOf(card.substring(0,1));
        }
        
    }
    /*
    A method to determine the state of the inputted score, bust, blackjack, or continue
    @param, an integer representing the current score
    @return, An integer representing the status of the hand.
    */
    public static int next(int Score)
    {
        if(Score> 21)
        {
            return 0;
        }
        else if (Score==21)
        {
            return 1;
        }
        else
        {
            return 2;
        }
        
    }
    
    
    
}

Player.java:
-----------
/*
This class creats a player object
@param, a String representing the name, an integer with the chip amount, and an integer with the players rank
@return, a Player object.
*/
public class Player
{
    private String name;
    private int chips;
    private int rank;
    
    /*
    this is a constructor for the Player class
    @param, a String representing the name instance variable, an integer representing chips and an integer for the players rank
    @return, none, a player object
    */
    public Player(String name, int chips, int rank)
    {
        this.name = name;
        this.chips = chips;
        this.rank = rank;
    }
    
    /*
    setter method for the name variable
    @param, String for the new name
    @return, none, void
    */
    public void setName(String NewName)
    {
        this.name = NewName;
    }
    /*
    getter method for the chip variable
    @param, none
    @return,the chip integer
    */
    public int getChips()
    {
        return this.chips;
    }
    /*
    setter method for the chips variable
    @param, Integer for the new chip amount
    @return, none, void
    */
    public void setChips(int NewChips)
    {
        this.chips = NewChips;
    }
    /*
    setter method for the rank variable
    @param, Integer for the new rank amount
    @return, none, void
    */
    public void setRank(int NewRank)
    {
        this.rank = NewRank;
    }
    /*
    getter method for the rank variable
    @param, none
    @return,the rank integer
    */
    public int getRank()
    {
        return this.rank;
    }
    /*
    A to string that prints the players, name, rank, and chips
    @param, none
    @return, a constructed string
    */
    public String toString()
    {
        return ("--PLAYER--"+"\n"+"Name: "+ this.name+"\n"+"Chips: "+this.chips+"\n"+"Rank: "+this.rank+"\n"+"----------");
    }
    
}

