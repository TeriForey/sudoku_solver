#!/usr/bin/env python

"""Tests for `sudoku_solver` package."""

import pytest


from sudoku_solver import solver


@pytest.fixture
def board():
    """
    Sudoku board for testing
    """
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    return board


def test_find_empty(board):
    """Test we can find the next empty cell"""
    res = solver.find_empty(board)
    assert res == (0, 2)


def test_valid_isvalid(board):
    """Test our validation"""
    res = solver.valid(board, 3, (0, 2))
    assert res is True


def test_valid_invalid_row(board):
    """Test validation of row"""
    res = solver.valid(board, 4, (0, 2))
    assert res is False


def test_valid_invalid_col(board):
    """Test validation of column"""
    res = solver.valid(board, 9, (0, 2))
    assert res is False


def test_valid_invalid_box(board):
    """Test validation of box"""
    res = solver.valid(board, 6, (0, 2))
    assert res is False


def test_solver(board):
    """Test solver can solve"""
    res = solver.solve(board)
    assert res is True
