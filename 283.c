void moveZeroes(int* nums, int numsSize) {
    int *w_ptr=nums; int *r_ptr=nums;
    int i=0, j=0;
    while(i<numsSize){
      if(*r_ptr!=0){
         *w_ptr=*r_ptr;
         *w_ptr++;
         j++;
      }
      r_ptr+=1;
      i++;
    }
    while(j<numsSize){
      *w_ptr=0;
      *w_ptr++;
      j++;
    }
}