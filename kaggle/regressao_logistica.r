require(rms)

#carregando dados
d <- read.csv("~/sid/usp/algo_am/porto/train.csv", header=T,dec=".", sep=",")
d_test <- read.csv("~/sid/usp/algo_am/porto/test.csv", header=T,dec=".", sep=",")
colnames(d)
summary(d[,3:ncol(d)])

#balanceamento manual
d_1 <- d[which(d$target==1),]
d_0a <- d[which(d$target==0),]
d_0 <- d_0a[1:nrow(d_1),]
dd <- rbind(d_1, d_0)
table(dd$target)

# modelo
#ps_ind_09_bin, ps_ind_14 <-- colunas problemáticas, investigar.
y <- target~ps_ind_01+ps_ind_02_cat+ps_ind_03+ps_ind_04_cat+ps_ind_05_cat+ps_ind_06_bin+ps_ind_07_bin+ps_ind_08_bin+ps_ind_10_bin+ps_ind_11_bin+ps_ind_12_bin+ps_ind_13_bin+ps_ind_15+ps_ind_16_bin+ps_ind_17_bin+ps_ind_18_bin+ps_reg_01+ps_reg_02+ps_reg_03+ps_car_01_cat+ps_car_02_cat+ps_car_03_cat+ps_car_04_cat+ps_car_05_cat+ps_car_06_cat+ps_car_07_cat+ps_car_08_cat+ps_car_09_cat+ps_car_10_cat+ps_car_11_cat+ps_car_11+ps_car_12+ps_car_13+ps_car_14+ps_car_15+ps_calc_01+ps_calc_02+ps_calc_03+ps_calc_04+ps_calc_05+ps_calc_06+ps_calc_07+ps_calc_08+ps_calc_09+ps_calc_10+ps_calc_11+ps_calc_12+ps_calc_13+ps_calc_14+ps_calc_15_bin+ps_calc_16_bin+ps_calc_17_bin+ps_calc_18_bin+ps_calc_19_bin+ps_calc_20_bin
m <- lrm(y, data=dd)
m

# avaliação nos dados de treinamento
p <- predict(m, data=dd, type="fitted")
y_pred <- round(p)
attach(dd)
table(target, y_pred)

# avaliação nos dados de teste
p <- predict(m, data=d_test, type="fitted")
y_pred <- round(p)
table(y_pred)

plot(p[1:100], pch=18, col="red", xlim=c(1,100), ylim=c(0,1), ylab="probs",xlab="amostra")
abline(h=0.5, col="green", lty=2)

