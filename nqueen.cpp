#include <iostream>
#define N 4 // Set board size to 8×8

using namespace std;

void printSolution(int board[N][N]) {
    static int solutionCount = 0;
    cout << "Solution " << ++solutionCount << ":\n";
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            cout << (board[i][j] ? "Q " : ". ");
        cout << endl;
    }
    cout << "\n";
}

bool isSafe(int board[N][N], int row, int col) {
    for (int i = 0; i < col; i++)
        if (board[row][i])
            return false;

    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    for (int i = row, j = col; i < N && j >= 0; i++, j--)
        if (board[i][j])
            return false;

    return true;
}

void solveNQueens(int board[N][N], int col, int &solutions) {
    if (col >= N) {
        printSolution(board);
        solutions++;
        return;
    }

    for (int i = 0; i < N; i++) {
        if (isSafe(board, i, col)) {
            board[i][col] = 1;
            solveNQueens(board, col + 1, solutions);
            board[i][col] = 0;
        }
    }
}

void nQueens() {
    int board[N][N] = {0};
    int solutions = 0;
    solveNQueens(board, 0, solutions);

    cout << "Total solutions for " << N << "×" << N << " board: " << solutions << endl;
}

int main() {
    nQueens();
    return 0;
}