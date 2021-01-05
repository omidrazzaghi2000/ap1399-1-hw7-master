#include "traverse.h"

//helper value
DFSTraverseClass::DFSTraverseClass(){

}
std::vector<Board> DFSTraverseClass::DFSTraverse(Board  start , Board  goal , int numberOflevels,int level ,Direction formerDirection ){
    Board temp = start;
    if(level < numberOflevels && start.getTable()!=goal.getTable()){
        if(formerDirection!=Direction::DOWN && start.moveEmptyTile(Direction::UP) && !finished){
            // std::cout << "UP\n";
            // std::cout << level << std::endl;
            // start.disp();
            solution.push_back(start);
            DFSTraverse(start,goal,numberOflevels,level+1,Direction::UP);
            start = temp;
            
        }
        if(formerDirection != Direction::UP && start.moveEmptyTile(Direction::DOWN) && !finished){
            // std::cout << "DOWN\n";
            // std::cout << level << std::endl;
            // start.disp();
            solution.push_back(start);
            DFSTraverse(start,goal,numberOflevels,level+1,Direction::DOWN);
            start = temp;
            
            
        }
        if(formerDirection != Direction::RIGHT && start.moveEmptyTile(Direction::LEFT) && !finished){
            // std::cout << "LEFT\n";
            // std::cout << level << std::endl;
            // start.disp();
            solution.push_back(start);
            DFSTraverse(start,goal,numberOflevels,level+1,Direction::LEFT);
            start = temp;
            
        }
        if(formerDirection != Direction::LEFT && start.moveEmptyTile(Direction::RIGHT) && !finished){
            // std::cout << "RIGHT\n";
            // std::cout << level << std::endl;
            // start.disp();
            solution.push_back(start);
            DFSTraverse(start,goal,numberOflevels,level+1,Direction::RIGHT);
            start = temp;
        }
            if(solution.size() > 0)
            solution.pop_back();
            if(level == 0 && !finished){
                solution.erase(solution.begin(),solution.end());
                std::cout << "\u001b[41mOps I can't find solution";
                std::cout << "\u001b[0m\n";
            }
            // std::cout << "Erase all" << std::endl;
            // solution.erase(solution.begin() , solution.end());
    }else{
        if(start.getTable()==goal.getTable()){
            std::cout << "\u001b[42mI found it";
            std::cout << "\u001b[0m\n";
            // start.disp();
            // std::cout << "This is solution with "<< level <<" steps." << std::endl;
            // for (size_t i {0} ; i < solution.size() ; i++){
            //     solution.at(i).disp();
            // }
            finished=true;
            final_solution = solution;
            
            

        }
        if(level >= numberOflevels) {
            // std::cout << " Erase Leaf" << std::endl;
            solution.pop_back();
            
        }
        
        
    }
    
    return final_solution;
    
}
Node::Node(Board Table, Direction fatherDirection ){
    table = Table;
    Board temp = Table;
    for(size_t i {0} ; i < 4 ; i++){
        switch (i)
        {
        case 0:
            //UP
            if(fatherDirection != Direction::DOWN &&  Table.moveEmptyTile(Direction::UP)){
                
                UPchildPointer = std::make_shared<Board>(Table);
            }else UPchildPointer = nullptr;
            Table = temp;
            break;
        case 1:
            //DOWN
            if(fatherDirection != Direction::UP &&  Table.moveEmptyTile(Direction::DOWN)){
                DOWNchildPointer = std::make_shared<Board>(Table);
            }else DOWNchildPointer = nullptr;
            Table = temp;
        case 2:
            //LEFT
            if(fatherDirection != Direction::RIGHT &&  Table.moveEmptyTile(Direction::LEFT)){
                LEFTchildPointer = std::make_shared<Board>(Table);
            }else LEFTchildPointer = nullptr;
            Table = temp;
        case 3:
            //RIGHT
            if(fatherDirection != Direction::LEFT &&  Table.moveEmptyTile(Direction::RIGHT)){
                RIGHTchildPointer = std::make_shared<Board>(Table);
            }else RIGHTchildPointer = nullptr;
            Table = temp;
        default:
            break;
        }
    }
}

void Node::disp(){
    table.disp();
    if(UPchildPointer!=nullptr){
        printf("\u001b[41mUP");
        printf("\u001b[0m : \n");
        UPchildPointer->disp();
    }
    if(DOWNchildPointer!=nullptr){
        printf("\u001b[42mDOWN");
        printf("\u001b[0m : \n");
        DOWNchildPointer->disp();
    }
    if(LEFTchildPointer!=nullptr){
        printf("\u001b[43mLEFT");
        printf("\u001b[0m : \n");
        LEFTchildPointer->disp();
    }
    if(RIGHTchildPointer!=nullptr){
        printf("\u001b[44mRIGHT");
        printf("\u001b[0m : \n");
        RIGHTchildPointer->disp();
    }
}
std::vector<Node> getRow(Node root){
    std::vector<Node> row;
        if(root.UPchildPointer != nullptr){
            Node up{Node(*root.UPchildPointer.get(),Direction::UP)};
            up.fatherPointer = std::make_shared<Node>(root);
            row.push_back(up);
            // printf("\u001b[45m\n");
            // printf("\u001b[0m\n");
        }
        if(root.DOWNchildPointer != nullptr){
            Node down{Node(*root.DOWNchildPointer.get(),Direction::DOWN)};
            down.fatherPointer = std::make_shared<Node>(root);
            row.push_back(down);
            // printf("\u001b[45m\n");
            // printf("\u001b[0m\n");
        }
        if(root.LEFTchildPointer != nullptr){
            Node left{Node(*root.LEFTchildPointer.get(),Direction::LEFT)};
            left.fatherPointer = std::make_shared<Node>(root);
            row.push_back(left);
            // printf("\u001b[45m\n");
            // printf("\u001b[0m\n");
        }
        if(root.RIGHTchildPointer != nullptr){
            Node right{Node(*root.RIGHTchildPointer.get(),Direction::RIGHT)};
            right.fatherPointer = std::make_shared<Node>(root);
            row.push_back(right);
            // printf("\u001b[45m\n");
            // printf("\u001b[0m\n");
        }
        return row;
}

std::vector<Board> traceSolution(Node finalNode){
    std::vector<Board> solution;
    while(finalNode.fatherPointer != nullptr){
        solution.push_back(finalNode.table);
        finalNode = *finalNode.fatherPointer.get();
    }
    return solution;
}
int checkRow(std::vector<Node> row,Board goal){
    for(int i {0} ; i < (int)row.size() ; i++){
        if(row.at(i).table.getTable() == goal.getTable()){
            printf("\u001b[46mI found it");
            printf("\u001b[0m\n");
            return i;
        }
    }
    return -1;
}


std::vector<Board> BFSTraverse(Board start , Board goal,int numberOfLevel){
    bool isFinished=false;
    
    Node root {Node(start,Direction::NOTHING)};
    root.fatherPointer = nullptr;
    // root.disp();
    // printf("\u001b[45m\n");
    // printf("\u001b[0m\n");
    if(root.table.getTable() == goal.getTable()){
        isFinished = true;
    }
    std::vector<Node> row;
    row.push_back(root);
    Node finalNode;
    for(int levelCounter {0} ; levelCounter < numberOfLevel && !isFinished; levelCounter++){
        std::vector<Node> tempRow {getRow(row.at(0))};
            auto v = getRow(row.at(0));
            // for(size_t i {0} ; i < v.size() ; i++){
            //     v.at(i).disp();
            // }
        if(checkRow(v,goal)!= -1){
            isFinished = true;
            break;
        }
        for(size_t i{1} ; i < row.size() ; i++){
            auto v = getRow(row.at(i));

            // for(size_t i {0} ; i < v.size() ; i++){
            //     v.at(i).disp();
            // }

            if(checkRow(v,goal)!= -1){
                isFinished = true;
                finalNode = v.at(checkRow(v,goal));
                
                break;
            }
            tempRow.insert(tempRow.cend(),v.begin() , v.end());
            
        }
        row = tempRow;
        
    }
    if(isFinished){
    std::vector<Board> solution{traceSolution(finalNode)};
    start.disp();
    
    for(int i{(int)solution.size()-1} ; i >= 0 ; i --){
        std::cout << solution.size() - i << std::endl;
        solution.at(i).disp();
    }
    return solution;
    }
    else{
        std::vector<Board> nosolution;
        
        printf("\u001b[47mI could not found it with this level");
        printf("\u001b[0m\n");

        return nosolution;
    }
}

//A* 
int Huristic_score(Board currentState , Board goal){
    int h_score{0};//because of empty tile
    for(size_t i {0}; i < currentState.getBoardSize() ;i++){
        for(size_t j {0} ; j < currentState.getBoardSize() ; j++){
            if(currentState.getTable().at(i).at(j) != goal.getTable().at(i).at(j)){
                h_score++;
            }
        }
    }
    return h_score;
}
// std::vector<Node> updateA_StarFeatures(std::vector<Node> tempRow , Board goal , int levelCounter){
//     for(size_t i {0} ; i < tempRow.size() ; i++){
//         tempRow.at(i).a_star_feature.h_score = Huristic_score(tempRow.at(i).table,goal);
//         tempRow.at(i).a_star_feature.g_score = levelCounter+1;
//         tempRow.at(i).a_star_feature.f_score = tempRow.at(i).a_star_feature.h_score+
//                                     tempRow.at(i).a_star_feature.g_score;
//         // i.table.disp();
//         // printf("h : %d , g: %d , f : %d \n",i.a_star_feature.h_score,i.a_star_feature.g_score,i.a_star_feature.f_score);
//     }
//     auto lessFunction = [](Node a,Node b){return a.a_star_feature.f_score > b.a_star_feature.f_score;};
//     // printf("test : %d\n" , tempRow.at(0).a_star_feature.f_score);
//     std::priority_queue<Node,std::vector<Node>,decltype(lessFunction)> sortedNodes(tempRow.begin(),tempRow.end());
//     // printf("min_f : %d\n" , sortedNodes.top().a_star_feature.f_score);
//     std::vector<Node> returnVector;
//     for(size_t i {0} ; i < sortedNodes.size() ; i++){
//         returnVector.push_back(sortedNodes.top());
//     }
//     return returnVector;
// }
// void A_StarTraverse(Board start , Board goal , int numberOfLevel){
//     static bool isFinished=false;
    
//     Node root {Node(start,Direction::NOTHING)};
//     root.a_star_feature.h_score=Huristic_score(start,goal);
//     root.a_star_feature.g_score=0;
//     root.a_star_feature.f_score=root.a_star_feature.g_score+
//                                 root.a_star_feature.h_score;
//     root.fatherPointer = nullptr;
//     // root.disp();
//     // printf("\u001b[45m\n");
//     // printf("\u001b[0m\n");
//     if(root.table.getTable() == goal.getTable()){
//         isFinished = true;
//     }
//     std::vector<Node> row;
//     row.push_back(root);
//     Node finalNode;
//     for(int levelCounter {0} ; levelCounter < numberOfLevel && !isFinished; levelCounter++){
//         std::vector<Node> tempRow ;

//         for(size_t i{0} ; i < row.size() ; i++){
//             auto v = getRow(row.at(i));

//             // for(size_t i {0} ; i < v.size() ; i++){
//             //     v.at(i).table.disp();
//             // }

//             if(checkRow(v,goal)!= -1){
//                 isFinished = true;
                
//                 finalNode = v.at(checkRow(v,goal));
                
//                 break;
//             }
//             tempRow.insert(tempRow.cend(),v.begin() , v.end());
            
//         }
//         //A* features updating:
//         if(!isFinished){
//             row.erase(row.begin(),row.end());
        
//             row = (updateA_StarFeatures(tempRow,goal,levelCounter));
//             // for(auto i : row){
//             //     A_StarTraverse(i.table,goal,numberOfLevel-levelCounter);
//             // }
            
//         }
//         // row.at(0).table.disp();
//     }
//     if(isFinished){
    
//     std::vector<Board> solution{traceSolution(finalNode)};
//     start.disp();
//     for(int i{(int)solution.size()-1} ; i >= 0 ; i --){
//         std::cout << solution.size() - i << std::endl;
//         solution.at(i).disp();
//     }
//     }
//     else{
//         printf("\u001b[49mI could not found it with this level");
//         printf("\u001b[0m\n");
//     }
// }



// //Bi directional search
