'''
Tests for molssi math module
'''
import pytest
import molssi_devops_uf as md

@pytest.mark.parametrize("num_list, expected_mean",
        [([1,2,3,4,5],3),([0,2,4,6],3),([1,2,3,4],2.5)])
def test_many(num_list, expected_mean):
    assert md.mean(num_list) == expected_mean

def test_mean():
    '''
    Tests the mean function
    '''
    num_list = [1, 2, 3, 4, 5]
    observed = md.mean(num_list)
    expected = 3

    assert observed == expected
def test_mean_wrong_type():
    '''
    Tests the type of the mean fn
    '''
    test_input = "this is not a list, stupid"
    with pytest.raises(TypeError):
        md.mean(test_input)
