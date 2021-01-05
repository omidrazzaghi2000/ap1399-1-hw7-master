#ifndef TRAVERSE_H
#define TRAVERSE_H
#include <iostream>
#include <vector>
#include <queue>
#include <memory>
#include "board.h"
std::vector<Board> BFSTraverse(Board start , Board goal ,int numberOfLevel);
class DFSTraverseClass{
public:
    DFSTraverseClass();
    ~DFSTraverseClass()=default;
    std::vector<Board> DFSTraverse(Board  start , Board   goal  ,int numberOflevels, int level = 0  ,Direction formerDirection=Direction::NOTHING );
private:
    std::vector<Board> solution;
    std::vector<Board> final_solution;
    bool finished=false;
};

class Node{
    public:
        std::shared_ptr<Node> fatherPointer;
        std::shared_ptr<Board> UPchildPointer;
        std::shared_ptr<Board> DOWNchildPointer;
        std::shared_ptr<Board> LEFTchildPointer;
        std::shared_ptr<Board> RIGHTchildPointer;
        Board table;
        Node(Board table , Direction);
        Node()=default;
        ~Node()=default;
        void disp();

    
};
#endif