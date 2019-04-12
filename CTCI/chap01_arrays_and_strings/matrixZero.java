class matrixZero {
    public void setZeroes(int[][] matrix) {

        if(matrix.length==0){
            return;
        }
        if(matrix[0].length==0){
            return;
        }

        int numrows = matrix.length;
        int numcols = matrix[0].length;

        int[] rows = new int[numrows];
        int[] cols = new int[numcols];

        for(int i=0; i<numrows; i++){
            for(int j=0; j<numcols; j++){
                if (matrix[i][j]==0){
                    rows[i]=1;
                    cols[j]=1;
                }
            }
        }

        for(int i=0; i<numrows; i++){
            if (rows[i]==1){
            for(int j=0; j<numcols; j++){
                matrix[i][j]=0;
                }
            }
        }

        for(int j=0; j<numcols; j++){
            if (cols[j]==1){
            for(int i=0; i<numrows; i++){
                matrix[i][j]=0;
                }
            }
        }
    }
}
