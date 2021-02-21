CREATE TABLE `Users` (
	`user_id`	varchar(20)	NOT NULL,
	`user_email`	varchar(255)	NOT NULL,
	`user_name`	varchar(255)	NOT NULL,
	`user_password`	varchar(255)	NOT NULL,
	`user_hp`	varchar(11)	NOT NULL,
	`user_nickname`	varchar(255)	NOT NULL,
	`email_certify`	datetime	NOT NULL,
	`lost_certify`	datetime	NOT NULL,
	`leave_flag`	char(1)	NOT NULL,
	`leave_date`	date	NOT NULL
);

CREATE TABLE `business` (
	`business_id`	int	NOT NULL,
	`category_id`	int	NOT NULL,
	`business_name`	varchar(255)	NOT NULL,
	`business_addr`	varchar(255)	NOT NULL,
	`business_tel`	varchar(11)	NOT NULL,
	`business_like`	int	NOT NULL
);

CREATE TABLE `like` (
	`like_id`	int	NOT NULL,
	`business_id`	int	NOT NULL,
	`user_id`	varchar(20)	NOT NULL,
	`like_time`	datetime	NOT NULL
);

CREATE TABLE `review` (
	`review_id`	int	NOT NULL,
	`business_id`	int	NOT NULL,
	`user_id2`	varchar(20)	NOT NULL,
	`review_time`	datetime	NOT NULL,
	`review_score`	int(1)	NOT NULL,
	`content`	text	NOT NULL
);

CREATE TABLE `category` (
	`category_id`	int	NOT NULL,
	`category_name`	varchar(255)	NOT NULL
);

CREATE TABLE `review_business_join` (
	`review_id`	int	NOT NULL,
	`business_id`	int	NOT NULL
);

CREATE TABLE `like_business_join` (
	`like_id`	int	NOT NULL,
	`business_id`	int	NOT NULL
);

ALTER TABLE `Users` ADD CONSTRAINT `PK_USERS` PRIMARY KEY (
	`user_id`
);

ALTER TABLE `business` ADD CONSTRAINT `PK_BUSINESS` PRIMARY KEY (
	`business_id`
);

ALTER TABLE `like` ADD CONSTRAINT `PK_LIKE` PRIMARY KEY (
	`like_id`
);

ALTER TABLE `review` ADD CONSTRAINT `PK_REVIEW` PRIMARY KEY (
	`review_id`
);

ALTER TABLE `category` ADD CONSTRAINT `PK_CATEGORY` PRIMARY KEY (
	`category_id`
);

ALTER TABLE `review_business_join` ADD CONSTRAINT `PK_REVIEW_BUSINESS_JOIN` PRIMARY KEY (
	`review_id`,
	`business_id`
);

ALTER TABLE `like_business_join` ADD CONSTRAINT `PK_LIKE_BUSINESS_JOIN` PRIMARY KEY (
	`like_id`,
	`business_id`
);

ALTER TABLE `review_business_join` ADD CONSTRAINT `FK_review_TO_review_business_join_1` FOREIGN KEY (
	`review_id`
)
REFERENCES `review` (
	`review_id`
);

ALTER TABLE `review_business_join` ADD CONSTRAINT `FK_business_TO_review_business_join_1` FOREIGN KEY (
	`business_id`
)
REFERENCES `business` (
	`business_id`
);

ALTER TABLE `like_business_join` ADD CONSTRAINT `FK_like_TO_like_business_join_1` FOREIGN KEY (
	`like_id`
)
REFERENCES `like` (
	`like_id`
);

ALTER TABLE `like_business_join` ADD CONSTRAINT `FK_business_TO_like_business_join_1` FOREIGN KEY (
	`business_id`
)
REFERENCES `business` (
	`business_id`
);
