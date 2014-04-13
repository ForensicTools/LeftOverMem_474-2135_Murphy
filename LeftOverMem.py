#LeftOverMem.py
#Catherine Murphy
#extention of volitity framework

minimum_size = None
alignment_gcd = None

def __init__(self, base, config, *args, **kwargs):
        self.base = base
        self.name = "Unnamed AddressSpace"
        self._config = config
        #list of memory segments
        self.seg = []
        self.header = None

def is_valid_address(self, _addr):
        return True

def address_mask(self, addr):
    return addr

def equal_address(self, a, b):
        return self.equal_address(a, b) == 0
        
#get memory info        
 def get_seg(self):
        return self.seg
        
        
#finding memory address in file         
def translate(self, addr):
        for input_addr, output_addr, length in self.seg:
            if (addr >= input_addr) and (addr < input_addr + length):
                return output_addr + (addr - input_addr)
            if addr < input_addr:
                return None
        return None
        
def valid_address(self, paddr):
        return self.translate(paddr) if not None


#to do
#create method to get all of memory addresses
#subtract the memory addreses we find from the memory
#create main menu and options
#print out and tie in everything together
   

