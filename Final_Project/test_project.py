import pytest
from project import load_data
from project import clean_data
from project import summarise_data


def test_load_data(tmp_path):
    content = """sample_id,group,absorbance
S001,control,0.412
S003,treatment,0.671
S004,control,
S006,treatment,invalid"""
    expected = [
        {'sample_id': 'S001', 'group': 'control', 'absorbance': '0.412'},
        {'sample_id': 'S003', 'group': 'treatment', 'absorbance': '0.671'},
        {'sample_id': 'S004', 'group': 'control', 'absorbance': ''},
        {'sample_id': 'S006', 'group': 'treatment', 'absorbance': 'invalid'}
        ]
    
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test.csv"
    p.write_text(content)
    result = load_data(p)
    assert result == expected 


    with pytest.raises(FileNotFoundError):              
        load_data("thisfiledoesnotexist.csv")


def test_clean_data():
    initial = [
        {'sample_id': 'S001', 'group': 'control', 'absorbance': '0.412'},
        {'sample_id': 'S002', 'group': 'control', 'absorbance': '0.398'},
        {'sample_id': 'S003', 'group': 'treatment', 'absorbance': '0.671'},
        {'sample_id': 'S004', 'group': 'control', 'absorbance': ''},
        {'sample_id': 'S005', 'group': 'treatment', 'absorbance': '0.702'},
        {'sample_id': 'S006', 'group': 'treatment', 'absorbance': 'invalid'}
        ]
    expected = [
        {'sample_id': 'S001', 'group': 'control', 'absorbance': 0.412},
        {'sample_id': 'S002', 'group': 'control', 'absorbance': 0.398},
        {'sample_id': 'S003', 'group': 'treatment', 'absorbance': 0.671},
        {'sample_id': 'S005', 'group': 'treatment', 'absorbance': 0.702},
        ]

    assert clean_data(initial) == expected
    
def test_summarise_data():
    initial = [
        {'sample_id': 'S001', 'group': 'control', 'absorbance': 0.412},
        {'sample_id': 'S002', 'group': 'control', 'absorbance': 0.398},
        {'sample_id': 'S003', 'group': 'treatment', 'absorbance': 0.671},
        {'sample_id': 'S005', 'group': 'treatment', 'absorbance': 0.702},
        ]
    expected = {'control': {'n': 2, 'mean': pytest.approx(0.405), 'stdev': pytest.approx(0.0098994949)}, 
                'treatment': {'n': 2, 'mean': pytest.approx(0.6865), 'stdev': pytest.approx(0.0219203102)}
                }

    assert summarise_data(initial) == expected

