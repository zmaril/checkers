import go 
import resource
resource.setrlimit(resource.RLIMIT_AS, (1000*1000*1000*50, -1L))
go.test_all_problems_G(4,10)
