test:
		pytest tests/

clean:
		find . | grep -E ".pytest_cache" | xargs rm -rf	
		find . | grep -E "__pycache__" | xargs rm -rf