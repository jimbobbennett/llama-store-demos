pip install build
cd ./llama-store/output/python
python -m build --outdir dist . 
pip install dist/llamastore-0.0.1-py3-none-any.whl