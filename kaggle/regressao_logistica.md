## Regressão Logistica - resultados

Carregando os dados:
````
d <- read.csv("~/sid/usp/algo_am/porto/train.csv", header=T,dec=".", sep=",")

````

Informações sobre o dataframe:
````
> colnames(d)
 [1] "id"             "target"         "ps_ind_01"      "ps_ind_02_cat"  "ps_ind_03"      "ps_ind_04_cat"  "ps_ind_05_cat"  "ps_ind_06_bin" 
 [9] "ps_ind_07_bin"  "ps_ind_08_bin"  "ps_ind_09_bin"  "ps_ind_10_bin"  "ps_ind_11_bin"  "ps_ind_12_bin"  "ps_ind_13_bin"  "ps_ind_14"     
[17] "ps_ind_15"      "ps_ind_16_bin"  "ps_ind_17_bin"  "ps_ind_18_bin"  "ps_reg_01"      "ps_reg_02"      "ps_reg_03"      "ps_car_01_cat" 
[25] "ps_car_02_cat"  "ps_car_03_cat"  "ps_car_04_cat"  "ps_car_05_cat"  "ps_car_06_cat"  "ps_car_07_cat"  "ps_car_08_cat"  "ps_car_09_cat" 
[33] "ps_car_10_cat"  "ps_car_11_cat"  "ps_car_11"      "ps_car_12"      "ps_car_13"      "ps_car_14"      "ps_car_15"      "ps_calc_01"    
[41] "ps_calc_02"     "ps_calc_03"     "ps_calc_04"     "ps_calc_05"     "ps_calc_06"     "ps_calc_07"     "ps_calc_08"     "ps_calc_09"    
[49] "ps_calc_10"     "ps_calc_11"     "ps_calc_12"     "ps_calc_13"     "ps_calc_14"     "ps_calc_15_bin" "ps_calc_16_bin" "ps_calc_17_bin"
[57] "ps_calc_18_bin" "ps_calc_19_bin" "ps_calc_20_bin"

> summary(d[,3:ncol(d)])
   ps_ind_01   ps_ind_02_cat      ps_ind_03      ps_ind_04_cat     ps_ind_05_cat     ps_ind_06_bin    ps_ind_07_bin   ps_ind_08_bin   
 Min.   :0.0   Min.   :-1.000   Min.   : 0.000   Min.   :-1.0000   Min.   :-1.0000   Min.   :0.0000   Min.   :0.000   Min.   :0.0000  
 1st Qu.:0.0   1st Qu.: 1.000   1st Qu.: 2.000   1st Qu.: 0.0000   1st Qu.: 0.0000   1st Qu.:0.0000   1st Qu.:0.000   1st Qu.:0.0000  
 Median :1.0   Median : 1.000   Median : 4.000   Median : 0.0000   Median : 0.0000   Median :0.0000   Median :0.000   Median :0.0000  
 Mean   :1.9   Mean   : 1.359   Mean   : 4.423   Mean   : 0.4168   Mean   : 0.4052   Mean   :0.3937   Mean   :0.257   Mean   :0.1639  
 3rd Qu.:3.0   3rd Qu.: 2.000   3rd Qu.: 6.000   3rd Qu.: 1.0000   3rd Qu.: 0.0000   3rd Qu.:1.0000   3rd Qu.:1.000   3rd Qu.:0.0000  
 Max.   :7.0   Max.   : 4.000   Max.   :11.000   Max.   : 1.0000   Max.   : 6.0000   Max.   :1.0000   Max.   :1.000   Max.   :1.0000  
 ps_ind_09_bin    ps_ind_10_bin      ps_ind_11_bin      ps_ind_12_bin      ps_ind_13_bin         ps_ind_14         ps_ind_15   
 Min.   :0.0000   Min.   :0.000000   Min.   :0.000000   Min.   :0.000000   Min.   :0.0000000   Min.   :0.00000   Min.   : 0.0  
 1st Qu.:0.0000   1st Qu.:0.000000   1st Qu.:0.000000   1st Qu.:0.000000   1st Qu.:0.0000000   1st Qu.:0.00000   1st Qu.: 5.0  
 Median :0.0000   Median :0.000000   Median :0.000000   Median :0.000000   Median :0.0000000   Median :0.00000   Median : 7.0  
 Mean   :0.1853   Mean   :0.000373   Mean   :0.001692   Mean   :0.009439   Mean   :0.0009476   Mean   :0.01245   Mean   : 7.3  
 3rd Qu.:0.0000   3rd Qu.:0.000000   3rd Qu.:0.000000   3rd Qu.:0.000000   3rd Qu.:0.0000000   3rd Qu.:0.00000   3rd Qu.:10.0  
 Max.   :1.0000   Max.   :1.000000   Max.   :1.000000   Max.   :1.000000   Max.   :1.0000000   Max.   :4.00000   Max.   :13.0  
 ps_ind_16_bin    ps_ind_17_bin    ps_ind_18_bin      ps_reg_01       ps_reg_02        ps_reg_03       ps_car_01_cat    ps_car_02_cat    
 Min.   :0.0000   Min.   :0.0000   Min.   :0.0000   Min.   :0.000   Min.   :0.0000   Min.   :-1.0000   Min.   :-1.000   Min.   :-1.0000  
 1st Qu.:0.0000   1st Qu.:0.0000   1st Qu.:0.0000   1st Qu.:0.400   1st Qu.:0.2000   1st Qu.: 0.5250   1st Qu.: 7.000   1st Qu.: 1.0000  
 Median :1.0000   Median :0.0000   Median :0.0000   Median :0.700   Median :0.3000   Median : 0.7207   Median : 7.000   Median : 1.0000  
 Mean   :0.6608   Mean   :0.1211   Mean   :0.1534   Mean   :0.611   Mean   :0.4392   Mean   : 0.5511   Mean   : 8.296   Mean   : 0.8299  
 3rd Qu.:1.0000   3rd Qu.:0.0000   3rd Qu.:0.0000   3rd Qu.:0.900   3rd Qu.:0.6000   3rd Qu.: 1.0000   3rd Qu.:11.000   3rd Qu.: 1.0000  
 Max.   :1.0000   Max.   :1.0000   Max.   :1.0000   Max.   :0.900   Max.   :1.8000   Max.   : 4.0379   Max.   :11.000   Max.   : 1.0000  
 ps_car_03_cat     ps_car_04_cat    ps_car_05_cat     ps_car_06_cat    ps_car_07_cat   ps_car_08_cat    ps_car_09_cat    ps_car_10_cat   
 Min.   :-1.0000   Min.   :0.0000   Min.   :-1.0000   Min.   : 0.000   Min.   :-1.00   Min.   :0.0000   Min.   :-1.000   Min.   :0.0000  
 1st Qu.:-1.0000   1st Qu.:0.0000   1st Qu.:-1.0000   1st Qu.: 1.000   1st Qu.: 1.00   1st Qu.:1.0000   1st Qu.: 0.000   1st Qu.:1.0000  
 Median :-1.0000   Median :0.0000   Median : 0.0000   Median : 7.000   Median : 1.00   Median :1.0000   Median : 2.000   Median :1.0000  
 Mean   :-0.5049   Mean   :0.7252   Mean   :-0.1577   Mean   : 6.555   Mean   : 0.91   Mean   :0.8321   Mean   : 1.329   Mean   :0.9921  
 3rd Qu.: 0.0000   3rd Qu.:0.0000   3rd Qu.: 1.0000   3rd Qu.:11.000   3rd Qu.: 1.00   3rd Qu.:1.0000   3rd Qu.: 2.000   3rd Qu.:1.0000  
 Max.   : 1.0000   Max.   :9.0000   Max.   : 1.0000   Max.   :17.000   Max.   : 1.00   Max.   :1.0000   Max.   : 4.000   Max.   :2.0000  
 ps_car_11_cat      ps_car_11        ps_car_12         ps_car_13        ps_car_14         ps_car_15       ps_calc_01       ps_calc_02    
 Min.   :  1.00   Min.   :-1.000   Min.   :-1.0000   Min.   :0.2506   Min.   :-1.0000   Min.   :0.000   Min.   :0.0000   Min.   :0.0000  
 1st Qu.: 32.00   1st Qu.: 2.000   1st Qu.: 0.3162   1st Qu.:0.6709   1st Qu.: 0.3332   1st Qu.:2.828   1st Qu.:0.2000   1st Qu.:0.2000  
 Median : 65.00   Median : 3.000   Median : 0.3742   Median :0.7658   Median : 0.3688   Median :3.317   Median :0.5000   Median :0.4000  
 Mean   : 62.22   Mean   : 2.346   Mean   : 0.3799   Mean   :0.8133   Mean   : 0.2763   Mean   :3.066   Mean   :0.4498   Mean   :0.4496  
 3rd Qu.: 93.00   3rd Qu.: 3.000   3rd Qu.: 0.4000   3rd Qu.:0.9062   3rd Qu.: 0.3965   3rd Qu.:3.606   3rd Qu.:0.7000   3rd Qu.:0.7000  
 Max.   :104.00   Max.   : 3.000   Max.   : 1.2649   Max.   :3.7206   Max.   : 0.6364   Max.   :3.742   Max.   :0.9000   Max.   :0.9000  
   ps_calc_03       ps_calc_04      ps_calc_05      ps_calc_06       ps_calc_07      ps_calc_08       ps_calc_09      ps_calc_10    
 Min.   :0.0000   Min.   :0.000   Min.   :0.000   Min.   : 0.000   Min.   :0.000   Min.   : 2.000   Min.   :0.000   Min.   : 0.000  
 1st Qu.:0.2000   1st Qu.:2.000   1st Qu.:1.000   1st Qu.: 7.000   1st Qu.:2.000   1st Qu.: 8.000   1st Qu.:1.000   1st Qu.: 6.000  
 Median :0.5000   Median :2.000   Median :2.000   Median : 8.000   Median :3.000   Median : 9.000   Median :2.000   Median : 8.000  
 Mean   :0.4498   Mean   :2.372   Mean   :1.886   Mean   : 7.689   Mean   :3.006   Mean   : 9.226   Mean   :2.339   Mean   : 8.434  
 3rd Qu.:0.7000   3rd Qu.:3.000   3rd Qu.:3.000   3rd Qu.: 9.000   3rd Qu.:4.000   3rd Qu.:10.000   3rd Qu.:3.000   3rd Qu.:10.000  
 Max.   :0.9000   Max.   :5.000   Max.   :6.000   Max.   :10.000   Max.   :9.000   Max.   :12.000   Max.   :7.000   Max.   :25.000  
   ps_calc_11       ps_calc_12       ps_calc_13       ps_calc_14     ps_calc_15_bin   ps_calc_16_bin   ps_calc_17_bin   ps_calc_18_bin  
 Min.   : 0.000   Min.   : 0.000   Min.   : 0.000   Min.   : 0.000   Min.   :0.0000   Min.   :0.0000   Min.   :0.0000   Min.   :0.0000  
 1st Qu.: 4.000   1st Qu.: 1.000   1st Qu.: 2.000   1st Qu.: 6.000   1st Qu.:0.0000   1st Qu.:0.0000   1st Qu.:0.0000   1st Qu.:0.0000  
 Median : 5.000   Median : 1.000   Median : 3.000   Median : 7.000   Median :0.0000   Median :1.0000   Median :1.0000   Median :0.0000  
 Mean   : 5.441   Mean   : 1.442   Mean   : 2.872   Mean   : 7.539   Mean   :0.1224   Mean   :0.6278   Mean   :0.5542   Mean   :0.2872  
 3rd Qu.: 7.000   3rd Qu.: 2.000   3rd Qu.: 4.000   3rd Qu.: 9.000   3rd Qu.:0.0000   3rd Qu.:1.0000   3rd Qu.:1.0000   3rd Qu.:1.0000  
 Max.   :19.000   Max.   :10.000   Max.   :13.000   Max.   :23.000   Max.   :1.0000   Max.   :1.0000   Max.   :1.0000   Max.   :1.0000  
 ps_calc_19_bin  ps_calc_20_bin  
 Min.   :0.000   Min.   :0.0000  
 1st Qu.:0.000   1st Qu.:0.0000  
 Median :0.000   Median :0.0000  
 Mean   :0.349   Mean   :0.1533  
 3rd Qu.:1.000   3rd Qu.:0.0000  
 Max.   :1.000   Max.   :1.0000  
 
````

Como as duas classes (campo target) estavam bem desbalanceadas, 1 = 21694 e 0 = 573502, peguei apenas 21694 exemplos com 0:

````
> d_1 <- d[which(d$target==1),]
> d_0a <- d[which(d$target==0),]
> d_0 <- d_0a[1:nrow(d_1),]
> dd <- rbind(d_1, d_0)
> table(dd$target)

    0     1 
21694 21694 

````

Treinando o modelo e coeficientes encontrados:

````
> y <- target~ps_ind_01+ps_ind_02_cat+ps_ind_03+ps_ind_04_cat+ps_ind_05_cat+ps_ind_06_bin+ps_ind_07_bin+ps_ind_08_bin+ps_ind_10_bin+ps_ind_11_bin+ps_ind_12_bin+ps_ind_13_bin+ps_ind_15+ps_ind_16_bin+ps_ind_17_bin+ps_ind_18_bin+ps_reg_01+ps_reg_02+ps_reg_03+ps_car_01_cat+ps_car_02_cat+ps_car_03_cat+ps_car_04_cat+ps_car_05_cat+ps_car_06_cat+ps_car_07_cat+ps_car_08_cat+ps_car_09_cat+ps_car_10_cat+ps_car_11_cat+ps_car_11+ps_car_12+ps_car_13+ps_car_14+ps_car_15+ps_calc_01+ps_calc_02+ps_calc_03+ps_calc_04+ps_calc_05+ps_calc_06+ps_calc_07+ps_calc_08+ps_calc_09+ps_calc_10+ps_calc_11+ps_calc_12+ps_calc_13+ps_calc_14+ps_calc_15_bin+ps_calc_16_bin+ps_calc_17_bin+ps_calc_18_bin+ps_calc_19_bin+ps_calc_20_bin
> m <- lrm(y, data=dd)
> m
Logistic Regression Model
 
 lrm(formula = y, data = dd)
 
                       Model Likelihood     Discrimination    Rank Discrim.    
                          Ratio Test           Indexes           Indexes       
 Obs         43388    LR chi2    2189.55    R2       0.066    C       0.628    
  0          21694    d.f.            55    g        0.521    Dxy     0.256    
  1          21694    Pr(> chi2) <0.0001    gr       1.684    gamma   0.256    
 max |deriv| 3e-08                          gp       0.124    tau-a   0.128    
                                            Brier    0.238                     
 
                Coef    S.E.   Wald Z Pr(>|Z|)
 Intercept      -0.9752 0.2117  -4.61 <0.0001 
 ps_ind_01       0.0133 0.0056   2.38 0.0175  
 ps_ind_02_cat   0.0619 0.0152   4.07 <0.0001 
 ps_ind_03       0.0140 0.0038   3.66 0.0003  
 ps_ind_04_cat   0.0433 0.0223   1.94 0.0527  
 ps_ind_05_cat   0.1002 0.0067  14.92 <0.0001 
 ps_ind_06_bin  -0.0302 0.0303  -1.00 0.3189  
 ps_ind_07_bin   0.2147 0.0328   6.54 <0.0001 
 ps_ind_08_bin   0.2182 0.0346   6.31 <0.0001 
 ps_ind_10_bin  -0.0203 0.4951  -0.04 0.9673  
 ps_ind_11_bin  -0.4727 0.2247  -2.10 0.0354  
 ps_ind_12_bin   0.0113 0.1018   0.11 0.9114  
 ps_ind_13_bin  -0.0368 0.3071  -0.12 0.9045  
 ps_ind_15      -0.0303 0.0032  -9.42 <0.0001 
 ps_ind_16_bin  -0.0186 0.0407  -0.46 0.6472  
 ps_ind_17_bin   0.3557 0.0473   7.52 <0.0001 
 ps_ind_18_bin   0.0445 0.0485   0.92 0.3592  
 ps_reg_01       0.1306 0.0463   2.82 0.0048  
 ps_reg_02       0.1062 0.0295   3.59 0.0003  
 ps_reg_03       0.1218 0.0172   7.09 <0.0001 
 ps_car_01_cat   0.0007 0.0043   0.16 0.8712  
 ps_car_02_cat  -0.0601 0.0307  -1.96 0.0502  
 ps_car_03_cat   0.0704 0.0178   3.96 <0.0001 
 ps_car_04_cat  -0.0174 0.0060  -2.90 0.0037  
 ps_car_05_cat   0.0230 0.0171   1.35 0.1779  
 ps_car_06_cat  -0.0039 0.0019  -2.01 0.0443  
 ps_car_07_cat  -0.3044 0.0275 -11.07 <0.0001 
 ps_car_08_cat   0.0184 0.0308   0.60 0.5496  
 ps_car_09_cat   0.0287 0.0131   2.20 0.0282  
 ps_car_10_cat  -0.1061 0.1095  -0.97 0.3322  
 ps_car_11_cat   0.0000 0.0003  -0.15 0.8819  
 ps_car_11      -0.0542 0.0124  -4.38 <0.0001 
 ps_car_12       0.9568 0.2762   3.46 0.0005  
 ps_car_13       0.4832 0.0988   4.89 <0.0001 
 ps_car_14      -0.0070 0.0279  -0.25 0.8029  
 ps_car_15       0.1134 0.0206   5.51 <0.0001 
 ps_calc_01      0.0512 0.0343   1.49 0.1354  
 ps_calc_02      0.0232 0.0345   0.67 0.5007  
 ps_calc_03      0.0189 0.0343   0.55 0.5816  
 ps_calc_04     -0.0011 0.0088  -0.12 0.9044  
 ps_calc_05     -0.0020 0.0086  -0.23 0.8159  
 ps_calc_06     -0.0021 0.0074  -0.28 0.7795  
 ps_calc_07      0.0027 0.0070   0.38 0.7032  
 ps_calc_08      0.0001 0.0067   0.02 0.9842  
 ps_calc_09      0.0031 0.0079   0.39 0.6991  
 ps_calc_10      0.0032 0.0034   0.93 0.3521  
 ps_calc_11     -0.0021 0.0042  -0.49 0.6212  
 ps_calc_12     -0.0045 0.0082  -0.55 0.5829  
 ps_calc_13     -0.0004 0.0059  -0.07 0.9481  
 ps_calc_14      0.0031 0.0036   0.88 0.3802  
 ps_calc_15_bin -0.0088 0.0300  -0.29 0.7688  
 ps_calc_16_bin  0.0127 0.0204   0.62 0.5340  
 ps_calc_17_bin  0.0009 0.0198   0.04 0.9652  
 ps_calc_18_bin -0.0147 0.0217  -0.68 0.4983  
 ps_calc_19_bin -0.0654 0.0206  -3.17 0.0015  
 ps_calc_20_bin  0.0066 0.0275   0.24 0.8093  

````

Avaliando no próprio conjunto de treinamento:

````
> p <- predict(m, data=dd, type="fitted")
> y_pred <- round(p)
> attach(dd)
> table(target, y_pred)
      y_pred
target     0     1
     0 13585  8109
     1  9629 12065
> Accuracy(y_pred, target)
[1] 0.5911773

````

Acurácia baixa, de 0.59, mesmo no conjunto de treinamento.


Plotando uma amostra:

````
> plot(p[1:100], pch=18, col="red", xlim=c(1,100), ylim=c(0,1), ylab="probs",xlab="amostra")
> abline(h=0.5, col="green", lty=2)

````
![Amostra Resultado Regressão Log](https://github.com/Superar/algoritmos-am/blob/master/kaggle/regressao_logistica01.png)

