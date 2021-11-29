CREATE TABLE history_user_like (
    id INT NOT NULL AUTO_INCREMENT,
    user_id int NOT NULL,
    property_id int NOT NULL,
    fecha_like TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES auth_user (id),
    FOREIGN KEY (property_id) REFERENCES property (id)
);