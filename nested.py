def outer():
	print("Inside Outer function");
	
	def Inner():
		print("Inside Inner function");
    
    return Inner;
		
def main():
		outer();
		
if __name__ == "__main__":
	main();