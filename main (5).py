#static method
class Mobile:
  @staticmethod
  def show_model(m,p):
    model = m
    price = p
    print("model:",m,"\nprice:",p)
    
r = Mobile()
Mobile.show_model('samsung',10000)