для работы по принципу TCR: 
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -e .

используйте @pytest.mark.xfail() чтобы падающий тест не откатил изменение
продвигаемся по одному юниттесту, достигнув осмысленного завершённого фрагмента работы меняем коммит и двигаемся дальше