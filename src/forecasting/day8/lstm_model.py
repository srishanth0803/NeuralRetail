import torch
import torch.nn as nn
import pytorch_lightning as pl

class LSTMForecast(pl.LightningModule):

    def __init__(self):

        super().__init__()

        self.lstm = nn.LSTM(
            input_size=1,
            hidden_size=64,
            num_layers=2,
            batch_first=True
        )

        self.fc = nn.Linear(
            64,
            3
        )

    def forward(self,x):

        out,(h,c)=self.lstm(x)

        output=self.fc(h[-1])

        return output

    def training_step(self,batch,batch_idx):

        x,y=batch

        pred=self(x)

        loss=nn.MSELoss()(pred,y)

        self.log(
            "train_loss",
            loss
        )

        return loss

    def configure_optimizers(self):

        optimizer=torch.optim.Adam(
            self.parameters(),
            lr=0.001
        )

        scheduler=torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(
            optimizer,
            T_0=10
        )

        return {
            "optimizer":optimizer,
            "lr_scheduler":scheduler
        }