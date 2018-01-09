1.# coding: utf-8  
2.  
3."""Train tickets query via command-line. 
4. 
5.Usage: 
6.    tickets [-gdtkz] <from> <to> <date> 
7. 
8.Options:  
9.    -h,--help        显示帮助菜单 
10.    -g               高铁 
11.    -d               动车 
12.    -t               特快 
13.    -k               快速 
14.    -z               直达 
15. 
16.Example: 
17.    tickets 南京 北京 2016-07-01 
18.    tickets -dg 南京 北京 2016-07-01 
19."""  
20.  
21.from docopt import docopt  
22.  
23.def cli():  
24.    """command-line interface"""   
25.    arguments = docopt(__doc__)  
26.    print(arguments)  
27.  
28.if __name__ == '__main__':   
29.    cli()  
