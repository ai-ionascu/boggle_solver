import unittest
import boggle
from string import ascii_uppercase

class test_boggle(unittest.TestCase):
    '''
    define test suite for boggle solver
    '''
    def test_if_can_create_empty_grid(self):
        '''
        test to see if an empty grid can be created
        '''
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid),0)
    
    def grid_size_is_width_times_height(self):
        '''
        make sure that the total size of the grid is equal to width * height
        '''
        grid = boggle.make_grid(2,3)
        self.assertEqual(len(grid),6)
        
    def test_grid_coordinates(self):
        '''
        make sure that all the coordinates inside the grid can be acessed
        '''
        grid = boggle.make_grid(2,2)
        self.assertIn((0,0),grid)
        self.assertIn((0,1),grid)
        self.assertIn((1,0),grid)
        self.assertIn((1,1),grid)
        self.assertNotIn((2,2),grid)
        
    def test_grid_contains_letters(self):
        '''
        make sure that the grid coordinates contain letters
        '''
        grid = boggle.make_grid(2,3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
            
    def test_neighbors_position(self):
        '''
        test that a position has 8 neighbors
        '''
        coords = (1,2)
        neighbors = boggle.get_neighbors(coords)
        self.assertIn((0,1), neighbors)
        self.assertIn((0,2), neighbors)
        self.assertIn((0,3), neighbors)
        self.assertIn((1,1), neighbors)
        self.assertIn((1,3), neighbors)
        self.assertIn((2,1), neighbors)
        self.assertIn((2,2), neighbors)
        self.assertIn((2,3), neighbors)
        
    def test_all_grid_coords_have_neighbors(self):
        '''
        make sure that every coordinate of the grid has neighbors
        '''
        # create a 2 x 2 grid where every coordinate has neighbors all the other coordinates of the grid
        
        grid = boggle.make_grid(2, 2)
        neighbors = boggle.all_grid_neighbors(grid)
        self.assertEqual(len(neighbors), len(grid))
        for pos in grid:
            others = list(grid)
            others.remove(pos)
            self.assertEqual(sorted(neighbors[pos]), sorted(others))
            
    def test_converting_a_path_to_a_word(self):
        """
        Ensure that paths can be converted to words
        """
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
        twoLetterWord = boggle.path_to_word(grid, [(0, 0), (1, 1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])
        
    def test_search_grid_for_words(self):
        '''
        make sure that certain words can be found in certain path patterns 
        within the grid
        '''
        grid = {(0,0):"A", (0,1):"B", (1,0):"C", (1,1):"D"}
        oneLetterWord = "A"
        twoLetterWord = "AB"
        threeLetterWord = "ABC"
        notThereWord = "EEE"
        fullWords = [oneLetterWord, twoLetterWord, threeLetterWord, notThereWord]
        partialWords = ["A", "AB", "E", "EE"]
        dictionary = fullWords, partialWords
        foundWords = boggle.search(grid, dictionary)
        
        self.assertTrue(oneLetterWord in foundWords)
        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)
        
    def test_load_dictionary(self):
        
        '''
        test if the "get_dictionary" function returns a dictionary 
        with a length greater than 0
        '''
        
        dictionary = boggle.get_dictionary("words.txt")
        self.assertGreater(len(dictionary), 0)
        
        