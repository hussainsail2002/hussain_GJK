import matplotlib.pyplot as plt
import numpy as np
import math

def mink_overall(tri1,tri2):
    mink_major=np.zeros(shape=(9,2))
    k=0
    for i in range(len(tri1)):
        for j in range (len(tri2)):
            mink_major[k]=np.subtract(tri2[i,:],tri1[j,:])
            k=k+1
        
    return mink_major

# This function normalizes a vector and points the vector in the opposite direction
def normalize_vect(new_vect):
    magnitude=np.linalg.norm(new_vect)
    norm_vect= (new_vect/magnitude)*-1
    return norm_vect

# This function takes a normal vector and then finds the highest/lowest dot product for each triangle
# and then creates the minkowski difference and returns the point that needs to be plotted
def sec_vect_length(norm_vect_1,tri1,tri2):
    dot_product_1=[]
    for i in range(0,3):
        dot_product_1.append(np.dot(norm_vect_1,tri1[i,:]))

    dot_product_2=[]
    for j in range(0,3):
        dot_product_2.append(np.dot(norm_vect_1,tri2[j,:]))

    #print(dot_product_1)
    #print(dot_product_2)
    pos1= dot_product_1.index(min(dot_product_1))
    pos2= dot_product_2.index(max(dot_product_2))
    #print(pos1)
    #print(pos2)
    new_point=np.subtract(tri2[pos2,:],tri1[pos1,:])
    #print(new_point)
    return new_point

def third_point(mink1,tri1,tri2):
    norm_vect=cross_product_func(mink1)
    da_point=sec_vect_length(norm_vect,tri1,tri2)
    return da_point


def cross_product_func(mink_vect):
    
    if len(mink_vect) > 2:
        mink_vect_1=np.append(mink_vect,[[0],[0],[0]],axis=1)
        vect_1=np.subtract(mink_vect_1[1,:],mink_vect_1[2,:])
        new_vect=np.cross(np.cross(mink_vect_1[1,:],mink_vect_1[2,:]),vect_1)
        new_vect=np.delete(new_vect,2,0)
        if np.dot(new_vect,mink_vect[0,:]) <= 0:
            final_vect=new_vect
        else:
            final_vect=new_vect*-1
        
        return final_vect
    
    else:
        mink_vect_1=np.append(mink_vect,[[0],[0]],axis=1)
        vect_1=np.subtract(mink_vect_1[0,:],mink_vect_1[1,:])
        vect_z=np.cross(mink_vect_1[0,:],mink_vect_1[1,:])
        new_vect=np.cross(vect_z,vect_1)
        new_vect=np.delete(new_vect,2,0)
        if np.dot(new_vect,mink_vect[0,:]) <= 0:
            final_vect=new_vect
        else:
            final_vect=new_vect*-1

        return final_vect
    
def cross_opposite(mink_vect):
    mink_vect_1=np.append(mink_vect,[[0],[0],[0]],axis=1)
    vect_1=np.subtract(mink_vect_1[0,:],mink_vect_1[2,:])
    new_vect=np.cross(np.cross(mink_vect_1[1,:],mink_vect_1[2,:]),vect_1)
    new_vect=np.delete(new_vect,2,0)
    if np.dot(new_vect,mink_vect[1,:]) <= 0:
        final_vect=new_vect
    else:
        final_vect=new_vect*-1


    return final_vect

def origin_check(mink_vector):
    normal_vect_1=cross_product_func(mink_vector)
    print(normal_vect_1)
    third_vect=mink_point[2,:]*-1
    normal_vect_2=cross_opposite(mink_vector)
    print (third_vect)

    if np.dot(normal_vect_1,third_vect) <=0: 
        return 1
    else:
        return 0

def third_point_origin_cross(mink_vect):
    mink_vect_1=np.append(mink_vect,[[0],[0],[0]],axis=1)
    vect_1=np.subtract(mink_vect_1[0,:],mink_vect_1[1,:])
    new_vect=np.cross(np.cross(mink_vect_1[1,:],mink_vect_1[2,:]),vect_1)
    new_vect=np.delete(new_vect,2,0)
    if np.dot(new_vect,mink_vect[0,:]) >= 0:
        final_vect=new_vect
    else:
        final_vect=new_vect*-1

    if np.dot(final_vect,mink_vect[2,:]) <=0:
        return 1
    else:
        return 0

    
    
fig,(ax1,ax2)=plt.subplots(1,2, figsize=(8,8))
tri_1=np.array([[1,1],[3,1],[3,3]])
tri_2=np.array([[3.2,2],[4,0],[6,2]])
ax2.set_xlim(-9,9)
ax2.set_ylim(-9,9)
ax2.set_box_aspect(1)
ax1.set_xlim(-9,9)
ax1.set_ylim(-9,9)
ax1.set_box_aspect(1)
ax1.title.set_text("Minkowski Space")
ax2.title.set_text("Cartesian 2D Space")
t1=plt.Polygon(tri_1[:,:],color="blue",fill=False)
t2=plt.Polygon(tri_2[:,:],color="blue",fill=False)
ax2.plot(0,0, marker="o", markersize=5,markeredgecolor="red")
ax2.add_patch(t1)
ax2.add_patch(t2)

#since we are using triangles we can get the entire minkowski space and check our solution.
total_mink=mink_overall(tri_1,tri_2)
#print (total_mink)

#angle_deg=random.randint(0,90)
# First random angle to choose a random vector
angle_deg=120
angle_rad=angle_deg*(math.pi/180)
x_vec=math.cos(angle_rad)
y_vec=math.sin(angle_rad)
base_vec=np.array([x_vec,y_vec])

# Creating the minkowski points by calling appropriate functions
mink_point=sec_vect_length(base_vec,tri_1,tri_2)
new_norm_vect=normalize_vect(mink_point)
mink_point=np.vstack((mink_point,sec_vect_length(new_norm_vect,tri_1,tri_2)))


# Since we have two minkowski points we can check if the second point has crossed the origin
# the dot product of the two vectors need to be less than 0
print(mink_point)
if np.dot(mink_point[0,:],mink_point[1,:]) <= 0:
    print(np.dot(mink_point[0,:],mink_point[1,:]))
    print ("Condition of second point is successful we shall continue")
else:
    print("Condition of second point has failed. There is no collision,program will terminate")
    ax1.plot(mink_point[:,0],mink_point[:,1],marker="o", markersize=5,markeredgecolor="red")
    plt.show()
    exit()

# now we need to find the third point

new_point_3=third_point(mink_point,tri_1,tri_2)
mink_point=np.vstack((mink_point,new_point_3))
#print (mink_point)

# Now that we have the thrid point we need to check if the third point has crosse the origin in the direction 
# perpendicular to the first two points. If it has not passed then it means that it does not contain the origin
# and we can quit the program.
#now that we have the third point we need to check if the triangle has enclosed the origin
cr_ori=third_point_origin_cross(mink_point)
if cr_ori==0:
    print('condition of the third point has failed. No collision,time to exit')
    t3=plt.Polygon(mink_point[:,:],color="blue",fill=False)
    ax1.add_patch(t3)
    ax1.scatter(mink_point[:,0],mink_point[:,1])
    ax1.plot(0,0, marker="o", markersize=5,markeredgecolor="red")
    plt.show()
    exit()

j=1
while j>0:
    i=origin_check(mink_point)
    print(mink_point)
    if i == 1:
        print("We have a collision")
        break
    else:
        print('No pass')
        temp_point=mink_point[0,:]
        mink_point=np.delete(mink_point,0,axis=0)
        new_point_3=third_point(mink_point,tri_1,tri_2)
        mink_point=np.vstack((mink_point,new_point_3))
        print(mink_point)
        cr_ori=third_point_origin_cross(mink_point)
        if cr_ori == 1:
            continue
        else:
            mink_point[2,:]=temp_point
            print("No collision here!")
            break

   
#print (mink_point)
t3=plt.Polygon(mink_point[:,:],color="blue",fill=False)
ax1.add_patch(t3)

ax1.plot(mink_point[0,0],mink_point[0,1], marker="o", markersize=5,markeredgecolor="red")
ax1.plot(mink_point[1,0],mink_point[1,1], marker="o", markersize=5,markeredgecolor="red")
ax1.plot(mink_point[2,0],mink_point[2,1], marker="o", markersize=5,markeredgecolor="red")
ax1.scatter(total_mink[:,0],total_mink[:,1])

ax1.plot(0,0, marker="o", markersize=5,markeredgecolor="red")
plt.show()