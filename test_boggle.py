import unittest
import boggle

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