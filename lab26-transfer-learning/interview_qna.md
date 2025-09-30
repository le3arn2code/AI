# Lab 26: Interview Q&A (Transfer Learning)

**Q1. What is transfer learning?**  
Transfer learning is the technique of using a pre-trained model on one task and adapting it to another related task.

**Q2. Why freeze layers in transfer learning?**  
To preserve learned features from the base model and reduce training cost.

**Q3. Which pre-trained models are commonly used?**  
Examples: VGG16, ResNet, Inception, MobileNet.

**Q4. What is fine-tuning?**  
Unfreezing some layers of the pre-trained model and retraining them with a smaller learning rate.

**Q5. Why use ImageNet-pretrained models?**  
They are trained on millions of images, providing strong general features.

**Q6. What loss function is used here?**  
Binary crossentropy, since we’re doing binary classification (cats vs. dogs).

**Q7. What optimizer is used here? Why?**  
Adam optimizer, because it adapts learning rate and converges fast.

**Q8. What is the role of ImageDataGenerator?**  
To rescale and feed images batch-wise from directories.

**Q9. Can transfer learning reduce overfitting?**  
Yes, because the base model brings generalized features instead of learning from scratch.

**Q10. What improvements can be made?**  
- Add dropout for regularization  
- Use data augmentation  
- Try deeper models or unfreeze more layers  
