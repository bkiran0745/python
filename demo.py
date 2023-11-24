import stakeholder as st
list1=["B Kiran","kkps",'100000',"bond paper",6949]
list2=["Kiran","Bs",'90000',"Stacks",4567]
st.insert(list1,list1[0])
st.insert(list2,list2[0])
st.Display(list1[0])
print("\n")
st.Display(list2[0])
print("\n")
st.display_all()
print("\n")
st.Delete(list2[0])
print("\n")
st.Edit_details(list1[0],3,1000000)
print("\n")
st.display_all()
print(st.validetion(list1[0],694))
st.sel_stak()

