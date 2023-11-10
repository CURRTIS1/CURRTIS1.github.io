## To learn

| Service| Done |
| ------ | ---- |
| AWS Storage Gateway | &#9745; |
| Dynamo DB Global or Secondary indexes | &#9744; |
| Dynamo DB partition or sort key | &#9744; |
| What is NOSQL | &#9744; |
| AWS Compute Optimizer | &#9744; |
| AWS S3 Storage Lens | &#9744; |
| Instance fleets | &#9744; |
| Kineses | &#9744; |
| ASG scaling methods (simple etc) | &#9744; |
| Endpoings (S3 test) | &#9744; |

Done - &#9745; <br>
Not done - &#9744;

## AWS Storage Gateway

AWS Storage Gateway is a set of hybrid cloud storage services that provide on-premises low latency access to virtually unlimited cloud storage.

Offerings:

- File Gateway
- Tape Gateway
- Volume Gateway

Fully Managed Cache: The local gateway appliance maintains a cache of recently written or read data so your applications can have low-latency access to data that is stored durably in AWS. The gateways use a read-through and write-back cache, committing data locally, acknowledging the write operations, and then asynchronously copying data to AWS, reducing application latency.

### AWS File Gateway

#### AWS S3 File Gateway

![fgws3](../../assets/images/fgws3.png "fgws3.png")

Amazon S3 File Gateway presents a file interface that enables you to store files as objects in Amazon S3 using the industry-standard NFS and SMB file protocols, and access those files via NFS and SMB from your data center or Amazon EC2, or access those files as objects directly in Amazon S3

#### AWS FSx File Gateway

![fgwfsx](../../assets/images/fgwfsx.png "fgwfsx.png")

Amazon FSx File Gateway provides fast, low-latency on-premises access to fully managed, highly reliable, and scalable file shares in the cloud using the industry-standard SMB protocol. Customers can store and access file data in Amazon FSx with Windows-native compatibility including full NTFS support, shadow copies, and Access Control Lists (ACLs).

### Tape Gateway

![tapegw](../../assets/images/tapegw.png "tapegw.png")

Back up and archive on-premises data to virtual tapes on AWS using your network. Use Tape Gateway to replace physical tapes on premises with virtual tapes on AWS—reducing your data storage costs without changing your tape-based backup workflows. Tape Gateway supports all leading backup applications and caches virtual tapes on premises for low-latency data access. It compresses your tape data, encrypts it, and stores it in a virtual tape library in Amazon Simple Storage Service (Amazon S3). From there, you can transfer it to either Amazon S3 Glacier Flexible Retrieval or Amazon S3 Glacier Deep Archive to help minimize your long-term storage costs.

### Volume Gateway

Volume Gateway presents cloud-backed iSCSI block storage volumes to your on-premises applications. Volume Gateway stores and manages on-premises data in Amazon S3 on your behalf and operates in either cache mode or stored mode. In the cached Volume Gateway mode, your primary data is stored in Amazon S3, while retaining your frequently accessed data locally in the cache for low latency access. In the stored Volume Gateway mode, your primary data is stored locally and your entire dataset is available for low latency access on premises while also asynchronously getting backed up to Amazon S3.

![volgw](../../assets/images/volgw.png "volgw.png")

## DynamoDB

### DynamoDB Primary Keys

You need a Primary Key on every row of your DynamoDB table and it has to be unique.

#### Partition Key

`Partition key`: A simple primary key, composed of one attribute known as the partition key. Attributes in DynamoDB are similar in many ways to fields or columns in other database systems.

Example would be `OrderID` as the `Partition Key` in the table below:

| OrderID | CustomerID | State | TotalAmount |
| ------- | ---------- | ----- | ----------- |
| 1 | CID-100 | SHIPPED | 3200 |
| 2 | CID-101 | DELIVERED | 700 |
| 3 | CID-100 | SHIPPED | 3 |
| 4 | CID-102 | DELIVERED | 12 |

The below is a table named 'People'.

```JSON
{
    "PersonID": 101,
    "LastName": "Smith",
    "FirstName": "Fred",
    "Phone": "555-4321"
}

{
    "PersonID": 102,
    "LastName": "Jones",
    "FirstName": "Mary",
    "Address": {
                "Street": "123 Main",
                "City": "Anytown",
                "State": "OH",
                "ZIPCode": 12345
    }
}

{
    "PersonID": 103,
    "LastName": "Stephens",
    "FirstName": "Howard",
    "Address": {
                "Street": "123 Main",
                "City": "London",                                    
                "PostalCode": "ER3 5K8"
    },
    "FavoriteColor": "Blue"
}
```

- Each item in the table has a unique identifier, or primary key, that distinguishes the item from all of the others in the table. In the People table, the `primary key` consists of one attribute (`PersonID`).
- Some of the items have a nested attribute (`Address`). DynamoDB supports nested attributes up to 32 levels deep.

#### Partition Key and Sort Key

`Partition key and sort key`: Referred to as a `composite primary key`, this type of key is composed of two attributes. The first attribute is the partition key, and the second attribute is the sort key. All data under a partition key is sorted by the sort key value.

The following is an example table named Music that you could use to keep track of your music collection:

```JSON
{
    "Artist": "No One You Know",
    "SongTitle": "My Dog Spot",
    "AlbumTitle": "Hey Now",
    "Price": 1.98,
    "Genre": "Country",
    "CriticRating": 8.4
}

{
    "Artist": "No One You Know",
    "SongTitle": "Somewhere Down The Road",
    "AlbumTitle": "Somewhat Famous",
    "Genre": "Country",
    "CriticRating": 8.4,
    "Year": 1984
}

{
    "Artist": "The Acme Band",
    "SongTitle": "Still in Love",
    "AlbumTitle": "The Buck Starts Here",
    "Price": 2.47,
    "Genre": "Rock",
    "PromotionInfo": {
        "RadioStationsPlaying": {
            "KHCR",
            "KQBX",
            "WTNR",
            "WJJH"
        },
        "TourDates": {
            "Seattle": "20150622",
            "Cleveland": "20150630"
        },
        "Rotation": "Heavy"
    }
}

{
    "Artist": "The Acme Band",
    "SongTitle": "Look Out, World",
    "AlbumTitle": "The Buck Starts Here",
    "Price": 0.99,
    "Genre": "Rock"
} 
```

The `primary key` for Music consists of `two attributes` (Artist and SongTitle). Each item in the table must have these two attributes. The combination of Artist and SongTitle distinguishes each item in the table from all of the others.

In a table that has a partition key and a sort key, it's possible for multiple items to have the same partition key value. However, those items must have different sort key values.

### DynamoDB Global or Secondary Index

You can create one or more secondary indexes on a table. A secondary index lets you query the data in the table using an alternate key, in addition to queries against the primary key. DynamoDB doesn't require that you use indexes, but they give your applications more flexibility when querying your data. After you create a secondary index on a table, you can read data from the index in much the same way as you do from the table.

DynamoDB supports two kinds of indexes:

- `Global secondary index` – An `index` with a `partition key` and `sort key` that can be different from those on the table.
- `Local secondary index` – An `index` that has the same `partition key` as the table, but a different `sort key`.

Each table in DynamoDB has a quota of 20 global secondary indexes (default quota) and 5 local secondary indexes.

Creating a Global Secondary Index creates a copy of the Primary table using the new partition key and keeps the two tables in sync.

If you have 1 Primary table and 5 Global Secondary Indexes, one write to the table actually equates to 5 as the changes have to be written to the GSIs.

You can only define a Local Secondary Index at the time of creating the table.

The following diagram shows the example `Music` table, with a new index called `GenreAlbumTitle`. In the index, `Genre` is the `partition key` and `AlbumTitle` is the `sort key`.

| Music Table | GenreAlbumTitle  |
| ----------- | ---------------- |
| <pre lang="json">{<br>  "Artist": "No One You Know",<br>  "SongTitle": "My Dog Spot",<br>  "AlbumTitle": "Hey Now",<br>  "Price": 1.98,<br>  "Genre": "Country",<br>  "CriticRating": 8.4<br>}</pre> | <pre lang="json">{<br>    "Genre": "Country",<br>    "AlbumTitle": "Hey Now",<br>    "Artist": "No One You Know",<br>    "SongTitle": "My Dog Spot"<br>}</pre> |
| <pre lang="json">{<br>    "Artist": "No One You Know",<br>    "SongTitle": "Somewhere Down The Road",<br>    "AlbumTitle": "Somewhat Famous",<br>    "Genre": "Country",<br>    "CriticRating": 8.4,<br>    "Year": 1984<br>}</pre> | <pre lang="json">{<br>    "Genre": "Country",<br>    "AlbumTitle": "Somewhat Famous",<br>    "Artist": "No One You Know",<br>    "SongTitle": "Somewhere Down The Road"<br>}</pre> |
| <pre lang="json">{<br>    "Artist": "The Acme Band",<br>    "SongTitle": "Still in Love",<br>    "AlbumTitle": "The Buck Starts Here",<br>    "Price": 2.47,<br>    "Genre": "Rock",<br>    "PromotionInfo": {<br>        "RadioStationsPlaying": {<br>            "KHCR",<br>            "KQBX",<br>            "WTNR",<br>            "WJJH"<br>        },<br>        "TourDates": {<br>            "Seattle": "20150622",<br>            "Cleveland": "20150630"<br>        },<br>        "Rotation": "Heavy"<br>    }<br>}</pre> | <pre lang="json">{<br>    "Genre": "Rock",<br>    "AlbumTitle": "The Buck Starts Here",<br>    "Artist": "The Acme Band",<br>    "SongTitle": "Still In Love"<br>}</pre> |
| <pre lang="json">{<br>    "Artist": "The Acme Band",<br>    "SongTitle": "Look Out, World",<br>    "AlbumTitle": "The Buck Starts Here",<br>    "Price": 0.99,<br>    "Genre": "Rock"<br>}</pre> | <pre lang="json">{<br>    "Genre": "Rock",<br>    "AlbumTitle": "The Buck Starts Here",<br>    "Artist": "The Acme Band",<br>    "SongTitle": "Look Out, World"<br>}</pre> |

| Index type | Description | Remember |
| ---------- | ----------- |--------- |
| Global Secondary Index | Partition key and sort key can be different from those on the table | Not restriced to just the partitioning set forth by the partition key, global |
| Local Secondary Index | Same partition key as the table but different sort key | Have to stay local and respect the tables partition key but can choose whatever sort key I want |

| Index type | When to use | Example |
| ---------- | ----------- |-------- |
| Global Secondary Index | When you want a fast query of attributes outside of the primary key | "I'd like to query sales orders by customer number rather than sales order number" |
| Local Secondary Index | When you already know the partition key and want to quickly query on another attribute | "I have the sales order number but I'd like to retrieve only those records with a certain Material number" |

You can query the GenreAlbumTitle index to find all albums of a particular genre (for example, all Rock albums). You can also query the index to find all albums within a particular genre that have certain album titles (for example, all Country albums with titles that start with the letter H).

```JSON
{
    "salesordernum" : "12346435",
    "timestamp" : "22-10-2023",
    "salesorder" : {
        "salesordertytpe" : "schedule",
        "materialnum" : "123217856"
    },
    "customer" : {
        "customernum" : "234235",
        "customername" : "Jimbob"
    }
}
```

If you created a Global Secondary Index using `customernum` you could query by Customer Number at light-speed.

If you created a Local Secondary Index using `materialnum` you could query bu Sales Order Number and Material Number at light-speed.

Attribute projections are attributes projected into an index, ie:

- customernum (key)
- customername
- salesordernum
- timestamp
- materialnum

You can also create a `replica` table by creating a `Global secondary index` using the same `partition key` and `sort key`. A use case for this would be if you wanted the same set of data present to higher and lower tier customers, you can set higher RCU/WCU limits for the higher tier customers.

![dynamo1](../../assets/images/dynamo1.png "dynamo1.png")

### DynamoDB scaling

Two ways to scale DynamoDB

- Throughput - based on RCU and WCUs
- Size - based on the storage size of data (max item is 400kb)

![dynkey](../../assets/images/dynkey.png "dynkey.png")

- Partition - a physical space where DynamoDB data is stored
- Partition key - a Unique identifier for each record, sometimes known as a Hash key
- Sort key - In combination with the partition key, optional second part of a composite key that defines storage order

Formula to decide on how many partitions are in a table:

| Method | Calculation | Note |
| ------ | ----------- | ---- |
| By Capacity | (Total RCU / 3000) + (Total WCU / 1000) | How many read units and write units are provisioned |
| By Size | Total Size / 10GB | Number of 10GB chunks the data takes up |
| Total Partitions | Round Up for the MAX (By Capacity, By Size) | The max of either of the above |

Example:

- 2000 RCUs
- 2000 WCUs
- 10GB Data

| Method | Calculation | Value |
| ------ | ----------- | ----- |
| By Capacity | (2000 / 3000) + (2000 / 1000) | 2.66 |
| By Size | Total Size / 10GB | 1 |
| Total Partitions | Round Up for the MAX (By Capacity, By Size) | 2.66 - So 3 partitions |

If you use say the Date as the partition key, and there's a lot of read/writes for that particular day then you end up with a `Hot partition` in that all traffic is only hitting the one partition:

![dynpartition1](../../assets/images/dynpartition1.png "dynpartition1.png")

A good idea would be to  use the sensor_id as the partition key which distributes the data across multiple partitions, and then use the date as the sort key.

![dynpartition2](../../assets/images/dynpartition2.png "dynpartition2.png")

### DynamoDB Streams

## ASG scaling methods

Step scaling methods don't have a cooldown period
