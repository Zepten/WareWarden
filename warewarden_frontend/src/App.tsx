import React, { useEffect, useState } from "react";
import Icon, {
  BellOutlined,
  DatabaseOutlined,
  PieChartOutlined,
  UserOutlined,
} from "@ant-design/icons";
import type { MenuProps } from "antd";
import {
  Avatar,
  Breadcrumb,
  Button,
  Flex,
  Layout,
  Menu,
  Table,
  theme,
} from "antd";
import axios from "axios";

type MenuItem = Required<MenuProps>["items"][number];

const { Header, Content, Footer, Sider } = Layout;

function getItem(
  label: React.ReactNode,
  key: React.Key,
  icon?: React.ReactNode,
  children?: MenuItem[],
): MenuItem {
  return {
    key,
    icon,
    children,
    label,
  } as MenuItem;
}

const items: MenuItem[] = [
  getItem("Главная", "dashboard", <PieChartOutlined />),
  getItem("Системные блоки", "pcs", <DatabaseOutlined />),
];

const App: React.FC = () => {
  const columns = [
    {
      title: "ID",
      dataIndex: "id",
      key: "id",
    },
    {
      title: "Название",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "Описание",
      dataIndex: "description",
      key: "description",
    },
    {
      title: "Дата создания",
      dataIndex: "created_at",
      key: "created_at",
    },
    {
      title: "Дата изменения",
      dataIndex: "modified_at",
      key: "modified_at",
    },
  ];

  const [pcs, setPcs] = useState([]);

  const fetchPcs = () => {
    axios.get(`/api/v1/pcs/`).then((response) => {
      const responseData = response.data;
      console.log(response);
      const pcsItems = responseData.map((pc: any) => {
        return {
          key: pc.uuid,
          id: pc.id,
          name: pc.name,
          description: pc.description,
          created_at: pc.created_at,
          modified_at: pc.modified_at,
        };
      });
      setPcs(pcsItems);
    });
  };

  useEffect(() => {
    fetchPcs();
  }, []);

  const [collapsed, setCollapsed] = useState(false);
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  return (
    <Layout style={{ minHeight: "100vh" }}>
      <Sider
        collapsible
        collapsed={collapsed}
        onCollapse={(value) => setCollapsed(value)}
      >
        <div className="demo-logo-vertical" />
        <Menu
          theme="dark"
          defaultSelectedKeys={["pcs"]}
          mode="inline"
          items={items}
        />
      </Sider>
      <Layout>
        <Header style={{ padding: 0, background: colorBgContainer }}>
          <Flex
            justify="flex-end"
            align="center"
            className="mr-3 mt-2"
            gap={10}
          >
            <Icon>
              <BellOutlined />
            </Icon>
            <Avatar size="large" icon={<UserOutlined />}></Avatar>
          </Flex>
        </Header>
        <Content style={{ margin: "0 16px" }}>
          <Breadcrumb style={{ margin: "16px 0" }}>
            <Breadcrumb.Item>Компьютеры</Breadcrumb.Item>
          </Breadcrumb>
          <div
            style={{
              padding: 24,
              minHeight: 360,
              background: colorBgContainer,
              borderRadius: borderRadiusLG,
            }}
          >
            <Button onClick={fetchPcs}>Обновить</Button>
            <Table dataSource={pcs} columns={columns} />
          </div>
        </Content>
        <Footer className="text-center">
          WareWarden © {new Date().getFullYear()} Made with 💖
        </Footer>
      </Layout>
    </Layout>
  );
};

export default App;
