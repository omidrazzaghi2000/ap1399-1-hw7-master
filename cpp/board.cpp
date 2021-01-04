#include <board.h>

#include <algorithm>//random_shuffle //swap
#include <ctime>//time
#include <cstdlib>//srand
#include <cstdio>//getchar


std::vector<int> getBoardSequenceFromUser(){
    std::cout << "Hello my friend (^_^) :" << std::endl;
    std::cout << "\tPlease enter your sequence like below template : "<< std::endl;
    std::cout << "\t4 3 2 1 5 6 0 7 8" << std::endl;
    std::cout << "\n\tThen we have this table :";
    std::cout << "\n\t\t\t 4 3 2 ";
    std::cout << "\n\t\t\t 1 5 6 ";
    std::cout << "\n\t\t\t 0 7 8 \n\n";
    std::cout << "Let's do this: ";
    char a[10];
    std::vector<int> Numbers;
    for(int i=0;; i++)
    {
        *(a+i*sizeof(char))=getchar();
        if((int)*(a+i*sizeof(char))!=32/*space*/ && (int)*(a+i*sizeof(char))!=-38){
            //check is correct or not is it duplicate or not or it has 0 or not check or valid number entered or did not 
            Numbers.push_back((int)*(a+i*sizeof(char))-48);
            
        }
        if(*(a+i*sizeof(char))=='\n')
        {
            *(a+i*sizeof(char))='\0';
            break;
        }

    }
    for(size_t i = 0 ; i < Numbers.size() ; i++){
      //I do not know but this for is important. 😮😮😮😮      
    }    
    return Numbers;
}

Board::Board(bool isRandom){


    
    std::vector<int> Numbers;
    if(isRandom){
        
        for(size_t i = 0 ; i < boardSize ; i++){
            for (size_t j = 0 ; j < boardSize ; j++){
                if((i==boardSize-1 && j == boardSize - 1 )){
                    //It is last emlement
                    Numbers.push_back(0);
                }else
                Numbers.push_back((j+1)+i*boardSize); 
            }
        }               
        srand((unsigned) time(0));
        std::random_shuffle ( Numbers.begin(), Numbers.end() );//scrambling
    }else{
        Numbers=getBoardSequenceFromUser();
    }
    //Add to table
    
        for(size_t i = 0 ; i < boardSize ; i++){
            std::vector<int> Row;
            for (size_t j = 0 ; j < boardSize ; j++){
                Row.push_back(Numbers.at((j)+i*boardSize));
            }
            Table.push_back(Row);
        }    
}
Board::Board(std::vector<int> Numbers,bool isRandom){
    for(size_t i = 0 ; i < boardSize ; i++){
            std::vector<int> Row;
            for (size_t j = 0 ; j < boardSize ; j++){
                Row.push_back(Numbers.at((j)+i*boardSize));
            }
            Table.push_back(Row);
        } 
}
void Board::disp(){
    std::cout << "The Board : " << std::endl;
    for(size_t i = 0 ; i < boardSize ; i++){
        for (size_t j = 0 ; j < boardSize ; j++){
            std::cout << std::right << std::setw(5)<<Table.at(i).at(j);
        }
        std::cout << std::endl;
    }
}
std::vector<int> find_tile_position(Board& b,int tileNumber){
    std::vector<int> position;
    for(size_t i = 0 ; i < b.getTable().size() ; i++){
        for (size_t j = 0 ; j < b.getTable().at(i).size() ; j++){
            if(b.getTable().at(i).at(j) == tileNumber){
                position.push_back(i);
                position.push_back(j);
                break;
            }
        }
    }
    //it does not found this tile :
    return position;
}
bool isThisPositionExist(Board& board,std::vector<int> position){
    return (position.at(0) >= 0 && position.at(1) >= 0) && (position.at(0) <= (int)board.getBoardSize()-1 && position.at(1) <= (int)board.getBoardSize()-1);
}
bool Board::moveEmptyTile(Direction direction){
    bool isSuccess=true;
    std::vector<int> zeroPosition=find_tile_position(*this,0);
    if(zeroPosition.size() == 2){
        std::vector<int> destinationPostion{zeroPosition};
        switch (direction){
            case Direction::UP:
                destinationPostion.at(0) -= 1;
                if(isThisPositionExist(*this,destinationPostion)){
                    std::swap(Table.at(zeroPosition.at(0)).at(zeroPosition.at(1)),
                              Table.at(destinationPostion.at(0)).at(destinationPostion.at(1)));
                }else{
                isSuccess = false;}
                break;
            case Direction::DOWN:
                destinationPostion.at(0) += 1;
                if(isThisPositionExist(*this,destinationPostion)){
                    std::swap(Table.at(zeroPosition.at(0)).at(zeroPosition.at(1)),
                              Table.at(destinationPostion.at(0)).at(destinationPostion.at(1)));
                }else{
                isSuccess = false;}
                break;
            case Direction::LEFT:
                destinationPostion.at(1) -= 1;
                if(isThisPositionExist(*this,destinationPostion)){
                     std::swap(Table.at(zeroPosition.at(0)).at(zeroPosition.at(1)),
                               Table.at(destinationPostion.at(0)).at(destinationPostion.at(1)));
                }else{
                isSuccess = false;}
                break;
            case Direction::RIGHT:
                destinationPostion.at(1) += 1;
                if(isThisPositionExist(*this,destinationPostion)){
                    std::swap(Table.at(zeroPosition.at(0)).at(zeroPosition.at(1)),
                              Table.at(destinationPostion.at(0)).at(destinationPostion.at(1)));
                }else{
                isSuccess = false;}
                break;
            case Direction::NOTHING:
                break;
        }
    }else{
        //[AnErrorOccured] : Zero tile is not in table
    }
    return isSuccess;
}
